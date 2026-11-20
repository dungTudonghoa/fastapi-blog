# ADR 0001 — Reconcile app and documentation histories

Status: Accepted, 2026-11-20.

Two unrelated Git histories existed: `main` contained a working HTML/JSON blog while `master` contained a minimal Hello World application plus documentation. Both were preserved through a non-fast-forward merge. The working blog in `src/fastapi_blog/` remains the application source of truth, and documentation/tests are updated to match it. The original root `main.py` and `src/main.py` are compatibility imports. Dependencies follow the blog configuration. Reason: preserve existing functionality and both commit histories without force-pushing or silently reverting the blog to Hello World. No new product feature is implied.
