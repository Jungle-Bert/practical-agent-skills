---
name: project-readme-first
description: Use Markdown first when entering, understanding, analyzing, debugging, reading, or modifying a project. Read AI_readme.md, README.md, and relevant Markdown before targeted configuration or source inspection. Create missing entry documents for authorized changes and keep them current. Applies to repositories, scripts, apps, services, and data projects.
---

# Project README First

Use existing project Markdown as the first source of context. `AI_readme.md` is the preferred source of AI navigation and constraints, but not the only one. Also read useful README, architecture, contribution, interface, and development documents relevant to the task. Inspect other files only when Markdown is insufficient; do not begin by reading the whole repository or source tree.

## Discover entry documents

1. Determine the target path requested by the user. If it is a subdirectory, use that as the initial scope. Check ancestor `.git` directories, build manifests, or package files only when needed to establish the project boundary.
2. Look for root Markdown in this order, tolerating filesystem case differences but using these canonical names when writing:
   - `AI_readme.md`: the AI project map, constraints, and recommended reading order.
   - `README.md`: the human-facing project overview, usage, and development entry point.
   - Other relevant Markdown, such as `ARCHITECTURE.md`, `CONTRIBUTING.md`, interface or design notes, and development notes.
3. Assess whether Markdown is useful: it should explain purpose, scope, layout, entry points, commands, dependencies, constraints, architecture, data flow, or the current issue. A changelog alone, an automatically generated index, or unrelated documents do not replace entry information.
4. Search deeper Markdown only when root documents do not provide enough useful information. Exclude `.git`, `node_modules`, `vendor`, `dist`, `build`, caches, and generated directories. Choose relevant documents closest to the target path and within the project.
5. For a repository with multiple projects, combine the nearest current-project Markdown with shared root documents. Do not use another subproject's README as the current project's entry point.

Example read-only search; filter results by document type, relevance, distance, and project boundary:

```powershell
rg --files -g '*.md' -g '!**/.git/**' -g '!**/node_modules/**' -g '!**/vendor/**' -g '!**/dist/**' -g '!**/build/**' <target-path>
```

## Reading order

1. If the current project has `AI_readme.md`, read it in full first. Extract purpose, current state, directory map, entry points, run and test commands, dependencies, environment, constraints, known pitfalls, and recommended reading.
2. Then read relevant README and other useful Markdown. If `AI_readme.md` is missing, start with README or the most relevant Markdown; do not skip existing information because a particular filename is absent.
3. Follow the documented reading order and task relevance. Prioritize entry points, architecture, interfaces, configuration notes, main flows, and tests. Read only relevant sections of large documents.
4. Inspect non-Markdown files only when the documents cannot answer the question. Use targeted searches, such as `rg -n` for a function, route, configuration key, command, or error, then open a small number of matching configuration, manifest, source, or test files.
5. Do not read all source, history, dependency source, generated files, or binaries by default. When expansion is necessary, explain what Markdown lacks and why a wider scope is needed, staying inside the project boundary.

## Missing entry documents

When `AI_readme.md` or `README.md` is missing:

- For authorized development, modification, or organization work, create the missing document at the project root. Create both if both are absent.
- For explicitly read-only reviews, questions, or status reports, do not write without authorization. Report the missing entry documents and add them after the user authorizes it.
- Read and use other useful Markdown first. Only when it is insufficient, gather facts from minimal directory listings, manifests, or other files. Mark unknowns as unconfirmed; do not invent commands, architecture, or constraints.
- After creating the documents, read `AI_readme.md` before continuing.

`README.md` should cover at least:

- Purpose, intended audience, and current state.
- Quick start, dependencies, environment variables, and common commands.
- Main features or workflows.
- Directory and module overview.
- Development, testing, build, deployment, and troubleshooting entry points.

`AI_readme.md` should cover at least:

- Project boundary, purpose, state, and sources of facts.
- Entry points, key directories or modules, and their responsibilities.
- Recommended reading, prioritizing relevant Markdown, with paths and reasons to read.
- Run, test, and build commands and prerequisites.
- Key dependencies, configuration, data flow, or call chains.
- Modification constraints, invariants, generated or non-editable directories, and known pitfalls.
- Checks required before completing a task.
- `Last verified` or an equivalent verification date and scope.

## Project changes

1. Before changing code, configuration, documentation, or data processing, read `AI_readme.md` if present, then README and relevant Markdown to identify the correct entry points, constraints, and checks.
2. Locate the change and its callers or tests with targeted searches. Do not infer impact from filenames alone.
3. Make the smallest necessary change, following documented generation, formatting, migration, and compatibility rules.
4. Run relevant tests, checks, or builds from the `AI_readme.md` checklist. Record why any check cannot run.
5. Update `AI_readme.md` when architecture, entry points, commands, directory responsibilities, configuration, constraints, or reading order change. Update README when human usage or development workflows change.
6. Update verification dates and known limitations so navigation does not contradict the code.

## Documentation maintenance

- Markdown is the first source of project context. `AI_readme.md` is preferred navigation, but is neither the only source nor the code itself. Cross-check relevant Markdown; use verifiable configuration, manifests, source, and tests for unresolved conflicts or gaps, then correct the documents.
- Keep `AI_readme.md` short and navigable: record where to look, why, and how to verify. Do not duplicate large source excerpts or API manuals.
- Use stable paths relative to the project root and explain their purpose. Avoid machine-specific absolute paths and invented secret values.
- Order recommended reading by its navigation value, prioritizing entry documents, architecture or interface notes, main flows, and tests.
- When multiple entry documents exist, state each one's project scope and link to other subproject entry documents.
