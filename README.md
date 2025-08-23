# Student Starter

A minimal Python starter for students: simple function, unit test, and CI.

## What’s inside
- `src/main.py` — app entry with a small `greet` function
- `tests/test_main.py` — unit test using `pytest`
- GitHub Actions workflow to run tests on every push/PR
- MIT license and a sane `.gitignore`

## Quick start
```bash
python -m venv .venv
# Windows PowerShell:
. .venv/Scripts/Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q
python src/main.py
```

## Contributing
1. Fork ➜ create a feature branch ➜ commit
2. `pytest -q` should pass locally
3. Open a Pull Request
