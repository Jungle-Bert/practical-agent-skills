# Capture and Maintenance

Read only when adding, revising, deduplicating, or repairing metadata, not for ordinary queries.

1. Search symptoms/cause/components through compact metadata and read at most the most relevant existing card. Update for the same cause and scope; create linked cards for different causes despite similar symptoms. A reusable first occurrence qualifies without recurrence across chats.
2. Cards use `entries/PIT-YYYYMMDD-short-slug.md`; IDs are unique and dates follow the user's timezone. Migrated legacy IDs preserve bodies, qualifiers, and sources. Do not bulk rewrite them.
3. Follow [entry-template.md](entry-template.md). Distinguish software checks, hardware evidence, and hypothesized causes. A code edit or “it should work” is not verification. Actual tests/builds or explicit successful user feedback support their demonstrated scope.
4. Do not capture ordinary questions. Save unresolved issues as pending only on request. Avoid unchanged duplicate entries; preserve historical conditions when recording counterexamples or obsolete solutions.
5. Exclude credentials and unnecessary personal data. Cite actual chat titles/links or files; do not invent task IDs, sources, or test outcomes.
6. Reread the selected card before writing and merge concurrent changes. The index is not a second detailed database. Maintain only the short fields below. Direction and boundaries must follow the card; retain qualifiers rather than claiming full resolution from partial verification.

Prepare metadata JSON in the current chat's work directory (replace example values):

```json
{
  "id": "PIT-20261002-example",
  "title": "Short issue title",
  "status": "Solution verified; cause unproven",
  "keywords": ["specific error code", "component", "中文症状", "English alias"],
  "direction": "One accurate fix or priority troubleshooting direction",
  "scope": "Environment, versions, and verification boundaries",
  "path": "entries/PIT-20261002-example.md"
}
```

7. After saving the card, run `python <skill>/scripts/pitfalls.py index --metadata <metadata.json>`. It reads only compact metadata and the selected card, hashes it, and preserves other records with an exclusive lock and atomic replacement. If locked, wait for the writer; do not remove the lock arbitrarily.
8. Read back with `get --id ...`. Check new content, unique IDs, and preservation of old entries before briefly reporting success. If metadata update fails, ingestion is incomplete even if the card exists. For `STALE_INDEX`, repair only the identified metadata; do not automatically rebuild the whole database.
9. index.jsonl contains one short record per line, no detailed bodies. Use at most 30 aliases of 2–100 characters; title ≤140, status ≤120, direction ≤220, scope ≤180 characters. Prefer specific components/functions/error codes and short bilingual aliases to reduce generic false matches.
