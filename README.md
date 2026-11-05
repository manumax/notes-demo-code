# Notes API

This repository contains the baseline FastAPI implementation described by the Product Knowledge Base in [`notes-demo-docs`](https://github.com/manumax/notes-demo-docs).

The API stores notes in memory. A note has an integer `id`, a non-empty `title`, non-empty `content`, and an optional list of `tags`. Each tag is a non-empty string; tags are matched exactly, including case and whitespace, and duplicate values on a note are stored once. `tags` is always present in responses and is empty when the note has none. Data is lost when the process stops.

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
curl -X POST http://127.0.0.1:8000/notes \
  -H 'content-type: application/json' \
  -d '{"title":"Shopping list","content":"Milk and coffee","tags":["personal","shopping"]}'
```

List notes:

```bash
curl http://127.0.0.1:8000/notes
```

List only notes that carry an exact tag:

```bash
curl 'http://127.0.0.1:8000/notes?tag=shopping'
```

Sending a note without `tags` creates or replaces it with no tags; `PUT /notes/{id}` replaces the note's tags entirely.

The implemented operations are:

- `GET /notes` — list notes, optionally filtered by one exact tag;
- `POST /notes` — create a note;
- `GET /notes/{id}` — retrieve a note;
- `PUT /notes/{id}` — replace a note;
- `DELETE /notes/{id}` — delete a note.
