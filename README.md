# Notes API

This repository contains the baseline FastAPI implementation described by the Product Knowledge Base in [`notes-demo-docs`](https://github.com/manumax/notes-demo-docs).

The API stores notes in memory. A note has an integer `id`, a non-empty `title`, and non-empty `content`. Data is lost when the process stops.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server listens on `http://127.0.0.1:8000`. FastAPI's interactive documentation is available at [`/docs`](http://127.0.0.1:8000/docs).

## Example

Create a note:

```bash
curl -X POST http://127.0.0.1:8000/notes \\
  -H 'content-type: application/json' \\
  -d '{"title":"Shopping list","content":"Milk and coffee"}'
```

List notes:

```bash
curl http://127.0.0.1:8000/notes
```

The implemented operations are:

- `GET /notes` — list notes;
- `POST /notes` — create a note;
- `GET /notes/{id}` — retrieve a note;
- `PUT /notes/{id}` — replace a note;
- `DELETE /notes/{id}` — delete a note.
