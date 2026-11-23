# Contributing

## Git workflow
1. Never commit straight to `main`. Make a branch:
   `feat/<thing>`, `fix/<thing>`, `docs/<thing>` or `hw/<thing>`.
2. Make small commits with clear messages, e.g. `feat(scout): add cliff sensor stop`.
3. Push and open a pull request. CI must pass before merging.
4. Update `docs/CHANGELOG.md` in the same PR, and `docs/HANDOFF.md` if the
   project's state changed.
5. Big decisions get a short record in `docs/decisions/` (copy an existing one).

## Never commit
Passwords, API keys, Wi-Fi credentials or `.env` files. Use `.env.example` with
fake values instead.

## Code style
- Python: `ruff check .` and `ruff format .`
- C++ firmware: clang-format (config added with the first firmware)
