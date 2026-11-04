# Agent Instructions — Notes API Implementation

## Mission

Maintain the small FastAPI implementation of the Notes API. The approved Product Knowledge Base in [`notes-demo-docs`](https://github.com/manumax/notes-demo-docs) is the behavior contract.

## Source of truth

- Read the product repository's `README.md` before changing API behavior. The implementation must match its model, routes, validation, status codes, and stated boundaries.
- Read the originating Issue and current Code PR discussion when working through the GitHub workflow. Tie implementation choices to the approved Product revision and Issue.
- Treat the current code as the implementation baseline, not as permission for unrelated refactoring.

## Implementation workflow

1. Inspect `main.py`, `requirements.txt`, this file, and the approved product README.
2. Map each requested behavior to the smallest set of implementation changes.
3. Preserve the existing FastAPI shape and in-memory storage unless the approved product specification changes them.
4. Keep route handlers, request models, response models, and error behavior aligned with the product contract.
5. Update the code README or dependency declarations only when the supported behavior or run instructions change.
6. Explain the Product PR/SHA used as the specification reference in the Code PR or change summary.

An implementation change is complete when the code covers every requested behavior, preserves the documented API contract, passes the available validation, and contains no unrelated refactoring.

## Baseline boundaries

- Keep the baseline intentionally small: FastAPI, in-memory note storage, and the five documented note operations.
- Preserve the `id`, `title`, and `content` model and the documented non-empty input rules unless the product specification explicitly changes them.
- Keep data loss on process restart; persistence, authentication, users, search, pagination, and unrelated infrastructure require an explicit product decision.
- Formal tests are outside the current MVP scope. Run smoke checks and add tests only when the request or repository workflow explicitly requires them.
- Work on the active feature branch. The AI edits and commits that branch; only a human approval command authorizes a merge to `main`.

## Validation

Use a repository-local virtual environment rather than changing the system Python. The baseline validation is:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m compileall -q .
```

When dependencies are available, start the app for a bounded smoke check and exercise create, list, retrieve, update, delete, validation, and not-found behavior. Stop the local server after validation. Report commands that could not run and why.

## Completion check

Before reporting completion, reread the approved product README, inspect the complete diff, verify every documented endpoint and status code, run the available validation, and state the Product revision used as the implementation reference.
