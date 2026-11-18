# Python Image Processor

A command-line tool for resizing, cropping, and converting images to grayscale.

## Features
- Resize an image while preserving its aspect ratio.
- Convert an image to grayscale.
- Process every supported image in a folder.
- Save processed files to a separate output folder.

## Requirements
- Python 3.10+
- Pillow

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python image_processor.py input.jpg --output output.jpg --grayscale
python image_processor.py input.jpg --output output.jpg --width 800
python image_processor.py ./photos --output-dir ./processed --grayscale
```

## Tests
```bash
pip install pytest
pytest
```

## What I learned
Image manipulation, command-line arguments, filesystem operations, reusable functions, and automated testing.
