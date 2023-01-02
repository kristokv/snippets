# snippets

## Install

If this is the first time using poetry set `poetry config virtualenvs.in-project true`, then run

```bash
poetry install
```

activate the environment with

```bash
poetry shell
# or
source .venv/bin/activate
```

to add it to jupyter run

```bash
python -m ipykernel install --user --name=snippets
```

**or** to just use `pip`

```bash
poetry export --without-hashes | pip install -r /dev/stdin
```
