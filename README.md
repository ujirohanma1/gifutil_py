# gifutil_py

A small Django app that converts animated GIFs into animated WebP images using Pillow.

## Features

- Upload an animated GIF through a web form
- Convert it to an animated WebP file
- Preview the converted WebP inline
- Download the converted file directly from the browser

## Requirements

- Python 3.8+ (recommended)
- Django
- Pillow with WebP support

## Installation

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
django
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Usage

- Open `http://127.0.0.1:8000/` in your browser
- Upload an animated GIF
- View the converted WebP preview
- Download the result as `converted.webp`

## Notes

- The conversion relies on Pillow and requires WebP support in the Pillow build.
- The app stores the converted image only in memory and does not save uploads to disk.
