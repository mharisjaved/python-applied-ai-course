# Environment Setup

Everything in this course runs on a normal laptop: **Python 3.13** (3.12 also works), **uv**, and **VS Code**
with the Python and Jupyter extensions. No GPU, no cloud account, and no paid API are required.

## 1. Install the tools (students did this on Day 01)

**uv** (official installer):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen the terminal, then check: `uv --version`.

**Python** is installed by uv on demand. To install it explicitly: `uv python install 3.13`.

**VS Code**: install from code.visualstudio.com, then the extensions **Python** (`ms-python.python`) and
**Jupyter** (`ms-toolsai.jupyter`).

## 2. Student setup (their own project, recommended)

Students keep one project folder for the whole course and add libraries when the course needs them.
This mirrors real development and is taught explicitly on Day 27.

```bash
uv init python-class          # Day 01
cd python-class
uv add ipykernel              # Day 02: lets VS Code run notebooks with this project's Python
uv add pytest                 # Day 29: testing
uv add numpy pandas matplotlib scikit-learn   # Day 43 (Week 9): data and machine learning
uv add anthropic python-dotenv                # Day 53 (Week 11): optional real LLM calls
```

Opening a notebook in VS Code: open the project folder (**File → Open Folder**), open or create an `.ipynb` file,
click **Select Kernel** (top right) → **Python Environments** → the one inside `.venv`. Run a cell with **Shift+Enter**.

Running a script: `uv run my_script.py` in the VS Code terminal.

## 3. Instructor setup (this course folder)

```bash
cd python-course
uv sync                       # creates .venv with everything in pyproject.toml / uv.lock
```

Open the folder in VS Code and select the `.venv` kernel for notebooks. Check everything works:

```bash
uv run python scripts/validate_notebooks.py weeks/week-01      # one week (about 1 minute)
uv run python scripts/validate_notebooks.py                    # whole course
```

Project reference implementations have their own tests, e.g.:

```bash
cd projects/03-expense-tracker/reference && uv run pytest -q
```

### Course environment contents (`pyproject.toml`)

| Package | Why | First used |
|---------|-----|-----------|
| `ipykernel` | run notebooks in VS Code | Day 02 |
| `pytest` | testing | Day 29 |
| `numpy`, `pandas`, `matplotlib`, `scikit-learn` | data analysis and ML | Days 43–50 |
| `anthropic`, `python-dotenv` | optional real LLM calls | Day 53 |
| `nbclient`, `nbformat` (dev group) | notebook validation script only | instructor |

Python: `.python-version` pins **3.13**; `requires-python = ">=3.12"`.

## 4. What to share with students

| Share | Keep private (instructor only) |
|-------|-------------------------------|
| `practice.ipynb` of each day (before or at the start of class) | `solutions.ipynb` |
| `demo.ipynb` (after class, as notes) | `projects/*/reference/`, `projects/*/INSTRUCTOR.md` |
| `projects/*/README.md` + `starter/` | answer keys in `assessments/` |
| `datasets/`, `concepts/` | |

Notebooks in later weeks read data with `Path("../../../datasets/…")` (three folders up from a day folder). If you
give students a single notebook, also give them the dataset and tell them to adjust that path (e.g. `Path("students.csv")`
when the file sits next to the notebook).

## 5. API keys (Week 11 onwards, optional)

Every LLM lesson and project works **offline with a mock model**. To use a real model:

1. Copy `.env.example` to `.env` (same folder as `pyproject.toml`) and paste the key after `ANTHROPIC_API_KEY=`.
2. Optionally set `LLM_MODEL`. The default is `claude-opus-5-5`; `claude-haiku-5-5` is much cheaper for a whole class.
3. Never commit `.env` (it is in `.gitignore`), never paste keys into notebooks, never share a key in chat.

For a classroom, the safest arrangement is: the instructor demos the real API live from their own machine; students
use the mock, or their own keys if they choose to create them.

## 6. Setup checklist (run before Day 02 and before Week 9)

- [ ] `uv --version` prints a version
- [ ] `uv run python --version` prints 3.12 or 3.13
- [ ] VS Code opens the project folder and a notebook cell runs with the `.venv` kernel
- [ ] Week 9+: `uv run python -c "import numpy, pandas, matplotlib, sklearn; print('ok')"` prints `ok`

Problems? See [troubleshooting.md](troubleshooting.md).
