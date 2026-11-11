# Plant Box (Leaf & Pot)

Plant Box is Leaf & Pot's new monthly plant subscription. This repo is an almost empty Flask
app: a home page, a base template and a database setup. You'll build Plant Box in it task by
task. Read `COMPANY.md` first: it has the founder's brief and the house rules.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its page: it has the rules
and the values (prices, discounts, names) for YOUR version. Every intern gets their own
version, so a solution copied from someone else will fail the tests.

## Run it
```
python -m venv .venv
.venv\Scripts\activate          # Windows (on macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
flask --app plantbox run --debug
```
Open http://127.0.0.1:5000. The database is `plantbox.sqlite`, created on start from
`plantbox/schema.sql`. Delete the file to start over.

## Test it
```
pytest
```
These tests are yours to run and extend. Darbni runs its own hidden tests on every submission.

## The AI rule
All AI calls go through `plantbox/ai.py`. Always call it like this:
```python
from plantbox import ai

reply = ai.ask_llm(prompt)
```
Not `from plantbox.ai import ask_llm`: Darbni's tests swap `ai.ask_llm` for a fake model, and
that import would keep the real one. `ask_llm` can fail, so always have a fallback text.

On your machine there is no real model: `ask_llm` returns a demo reply that starts with
`[Demo AI reply]`. To see what your page does when the AI is down, make it fail:
```
set PLANTBOX_AI=fail            # Windows cmd (PowerShell: $env:PLANTBOX_AI="fail")
export PLANTBOX_AI=fail         # macOS/Linux
flask --app plantbox run --debug
```
Unset it (or open a new terminal) to get the demo reply back.

## Where things are
| File | What it does |
|---|---|
| `plantbox/__init__.py` | `create_app(config)`: builds the app |
| `plantbox/pages.py` | the routes |
| `plantbox/db.py` | `db.connect()` for the SQLite database |
| `plantbox/schema.sql` | the tables, created on every start |
| `plantbox/ai.py` | `ask_llm(prompt)`, the only way to call AI |
| `plantbox/templates/` | `base.html` (header, footer) and one template per page |
| `plantbox/static/style.css` | the styles |
| `tests/` | pytest tests |
