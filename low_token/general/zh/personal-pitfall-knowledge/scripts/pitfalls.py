"""Search compact metadata, then read only a selected pitfall card."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys


def search(root, query, limit=3, max_chars=700):
    rows = load_index(root)
    ranked = []
    for row in rows:
        score = 0
        for term in set([row['id'], *row['keywords']]):
            term = term.casefold()
            if contains(query.casefold(), term):
                score += alias_weight(term)
        if score:
            ranked.append((score, row))
    ranked.sort(key=lambda item: (-item[0], item[1]['id']))
    if not ranked:
        return 'NO_MATCH'
    ranked = [item for item in ranked if item[0] >= ranked[0][0] * 0.6]
    blocks = []
    for _, row in ranked[:min(limit, 3)]:
        blocks.append(f"{row['id']} | {row['title']}\n{row['status']} | {row['direction']}\nScope: {row['scope']}")
    return bounded('\n\n'.join(blocks), max_chars)


def get(root, entry_id, max_chars=1600):
    row = next((row for row in load_index(root) if row['id'] == entry_id), None)
    if row is None:
        raise ValueError('Unknown entry ID; search first.')
    path = entry_path(root, row)
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != row['sha256']:
        raise ValueError('STALE_INDEX: selected card changed; update its metadata before reuse.')
    return bounded(data.decode('utf-8'), max_chars)


def update_index(root, metadata):
    row = json.loads(Path(metadata).read_text(encoding='utf-8'))
    check_row(row, require_hash=False)
    row['sha256'] = hashlib.sha256(entry_path(root, row).read_bytes()).hexdigest()
    lock = root / '.index.lock'
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError('INDEX_BUSY: another writer holds the lock; retry after it finishes.') from None
    temp = root / f'.index-{os.getpid()}.tmp'
    try:
        os.close(descriptor)
        rows = load_index(root) if (root / 'index.jsonl').exists() else []
        rows = [old for old in rows if old['id'] != row['id']] + [row]
        rows.sort(key=lambda item: item['id'])
        temp.write_text(''.join(json.dumps(item, ensure_ascii=False) + '\n' for item in rows), encoding='utf-8')
        os.replace(temp, root / 'index.jsonl')
        return f"INDEXED {row['id']}"
    finally:
        temp.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def load_index(root):
    rows = []
    seen = set()
    with (root / 'index.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            if not line.strip():
                continue
            row = json.loads(line)
            check_row(row)
            if row['id'] in seen:
                raise ValueError('Duplicate ID in compact index.')
            seen.add(row['id'])
            rows.append(row)
    return rows


def check_row(row, require_hash=True):
    sizes = {'id': 90, 'title': 140, 'status': 120, 'direction': 220, 'scope': 180, 'path': 110}
    if not isinstance(row, dict):
        raise ValueError('Index record must be an object.')
    for field, size in sizes.items():
        if not isinstance(row.get(field), str) or not row[field].strip() or len(row[field]) > size:
            raise ValueError(f'Invalid compact metadata field: {field}')
    if not re.fullmatch(r'PIT-[A-Za-z0-9-]+', row['id']):
        raise ValueError('Invalid entry ID.')
    terms = row.get('keywords')
    if not isinstance(terms, list) or not 1 <= len(terms) <= 30:
        raise ValueError('Use 1-30 searchable aliases.')
    if any(not isinstance(term, str) or not 2 <= len(term.strip()) <= 100 for term in terms):
        raise ValueError('Invalid searchable alias.')
    if require_hash and not re.fullmatch(r'[0-9a-f]{64}', row.get('sha256', '')):
        raise ValueError('Missing card hash; update metadata.')


def entry_path(root, row):
    if row['path'] != f"entries/{row['id']}.md":
        raise ValueError('Card path must match its entry ID.')
    path = (root / row['path']).resolve()
    if not path.is_relative_to((root / 'entries').resolve()):
        raise ValueError('Card path escapes the entries directory.')
    return path


def contains(query, term):
    query, term = query.casefold(), term.casefold()
    if re.fullmatch(r'[a-z0-9_.+-]+', term):
        return bool(re.search(r'(?<![a-z0-9_])' + re.escape(term) + r'(?![a-z0-9_])', query))
    return term in query


def alias_weight(term):
    if re.fullmatch(r'[a-z]+\d{3,}', term):
        return 100
    if any(ch in term for ch in '._-'):
        return 50
    return 15 if len(term) >= 3 else 5


def bounded(text, max_chars):
    if len(text) <= max_chars:
        return text
    suffix = '\n[TRUNCATED: refine query or request a larger budget; never infer omitted text.]'
    return text[:max_chars - len(suffix)] + suffix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(os.environ.get('PITFALL_KB_ROOT', str(Path.home() / 'Documents/Codex/knowledge-base/pitfalls'))))
    commands = parser.add_subparsers(dest='command', required=True)
    lookup = commands.add_parser('search')
    lookup.add_argument('--query', required=True)
    lookup.add_argument('--limit', type=int, choices=range(1, 4), default=3)
    lookup.add_argument('--max-chars', type=int, default=700)
    detail = commands.add_parser('get')
    detail.add_argument('--id', required=True)
    detail.add_argument('--max-chars', type=int, default=1600)
    index = commands.add_parser('index')
    index.add_argument('--metadata', required=True)
    args = parser.parse_args()
    try:
        if args.command in ('search', 'get') and not 128 <= args.max_chars <= 4000:
            raise ValueError('Output budget must be between 128 and 4000 characters.')
        if args.command == 'search':
            result = search(args.root, args.query, args.limit, args.max_chars)
        elif args.command == 'get':
            result = get(args.root, args.id, args.max_chars)
        else:
            result = update_index(args.root, args.metadata)
        print(result)
    except (OSError, ValueError, KeyError, UnicodeError) as error:
        print(bounded('ERROR: ' + str(error), 500), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
