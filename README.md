# Notes API

This repository contains the baseline FastAPI implementation described by the Product Knowledge Base in [`notes-demo-docs`](https://github.com/manumax/notes-demo-docs).

The API stores notes in memory. A note has an integer `id`, a non-empty `title`, non-empty `content`, an optional list of `tags`, and a boolean `pinned` flag that defaults to `false` and is always present in responses. Each tag is a non-empty string; tags are matched exactly, including case and whitespace, and duplicate values on a note are stored once. `tags` is always present in responses and is empty when the note has none. Data is lost when the process stops.

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
  -d '{"title":"Shopping list","content":"Milk and coffee","tags":["personal","shopping"],"pinned":true}'
```

List notes:

```bash
curl http://127.0.0.1:8000/notes
```

Notes are returned with pinned notes first, then the remaining notes in ascending `id` order within each group.

List only notes that carry an exact tag:

```bash
curl 'http://127.0.0.1:8000/notes?tag=shopping'
```

Search titles with `q`:

```bash
curl 'http://127.0.0.1:8000/notes?q=milk'
```

`q` matches any note whose `title` contains it as a literal substring, ignoring case for the ASCII letters `A`–`Z` only: `q=MILK` matches titles containing `milk`, `Milk`, or `MILK`, while `q=cafe` does not match a title containing `Café`. Surrounding whitespace is trimmed from `q`, and an absent, empty, or whitespace-only `q` applies no title filter. Only `title` is searched; `content` and `tags` are never matched. Sending both filters returns only notes that satisfy both:

```bash
curl 'http://127.0.0.1:8000/notes?q=milk&tag=shopping'
```

Each filtered list keeps the same ordering: pinned notes first, then ascending `id` within each group. Sending a note without `tags` creates or replaces it with no tags; `PUT /notes/{id}` replaces the note's tags entirely and resets `pinned` to `false` when the field is omitted.

The implemented operations are:

- `GET /notes` — list notes, pinned first and then ascending `id`, optionally filtered by one exact tag and searched by title with `q`;
- `POST /notes` — create a note;
- `GET /notes/{id}` — retrieve a note;
- `PUT /notes/{id}` — replace a note;
- `DELETE /notes/{id}` — delete a note.
