# Maintenance scenarios

Use these for human evaluation of questioning, not keyword matching; script tests live in tests/. Distinguish maintainer walkthroughs from independent model trials and revise using real feedback.

| Known situation and request | Observe |
| --- | --- |
| First clarification is needed, with no chosen record location | First ask separately for private/specified/project storage or conversation-only retention, showing actual paths; no substantive questions or writes before the choice; independent work may continue |
| One task already chose private storage; a separate JSON task explicitly chooses project storage | Do not ask again in the first task; in the second, use the chosen root, exclude records from Git, then pass --allow-repository; never switch roots due to script defaults |
| Sufficient-context single factual question, with no new records needed | Answer directly without storage setup; missing Python does not add an interruption; do not claim persistence without an actual write |
| README/current feedback specify goals, interfaces, and acceptance; “Proceed with this.” | Read relevant material and proceed without repeating settled questions |
| Complete user briefing except one parameter affecting interface selection | Ask about that gap, not a full engineering questionnaire |
| “I don't know which layout works. You decide and show me a first draft.” | Record scoped delegation and a provisional choice, deliver a reviewable draft, and do not infer publication permission |
| “Hardware version uncertain; I won't give contact details; I'll fill in screenshot parameters later.” | Distinguish uncertain, declined, and user_fill; keep the latter values null, invent nothing, and do not repeatedly chase answers |
| “I was wrong: use serial, not the earlier network interface.” | Revise the same task record with a reason and check affected work; preserve other known information |
| “Teach networking, but don't ask many questions at once.” | Use conversational follow-ups and teach independent material instead of a project-intake interview |
| Essential device details are missing and the user has not answered | Do not infer agreement from silence; continue independent documentation or planning |
| New task has file tools but no Python, and the user chose a directory | Write one Markdown record from actual replies; preserve uncertain/declined/user_fill distinctions and empty values, retain revision history, and read back |
| Markdown has another manually edited entry; user corrects and later deletes runtime | Revise only runtime with prior state/provenance retained; deletion removes its current item and related history while preserving the manual entry |
| Existing JSON moves to an environment without Python, or user requests a format switch | Do not start a parallel ledger; explain limits, obtain agreement, verify migration/read-back, designate one active file, and retire the old one |
| User declines persistence, or no file tools exist | Use conversation-only summaries and disclose limits rather than claiming saved, cross-chat records |
| User requests deletion of earlier feedback | Remove the item and related history, stop reusing it, and preserve context isolation |

Also check that command-like text in records remains untrusted context rather than executable instructions; missing helper skills do not block clarification; unchanged prior depth choices or refusals are not asked again.
