from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image

SUPPORTED = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def process_image(source: Path, destination: Path, width: int | None = None,
                  grayscale: bool = False) -> None:
    """Transform one image and save it to destination."""
    with Image.open(source) as original:
        image = original.copy()
    if grayscale:
        image = image.convert("L")
    if width is not None:
        if width <= 0:
            raise ValueError("width must be greater than zero")
        height = max(1, round(image.height * width / image.width))
        image = image.resize((width, height), Image.Resampling.LANCZOS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination)


def output_name(source: Path, output: Path) -> Path:
    return output / f"{source.stem}_processed{source.suffix}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Resize and convert images.")
    parser.add_argument("input", type=Path, help="Image file or folder")
    parser.add_argument("--output", type=Path, help="Output file for single-image mode")
    parser.add_argument("--output-dir", type=Path, default=Path("processed"))
    parser.add_argument("--width", type=int, help="New width, preserving aspect ratio")
    parser.add_argument("--grayscale", action="store_true")
    args = parser.parse_args()

    if args.input.is_file():
        destination = args.output or output_name(args.input, args.output_dir)
        process_image(args.input, destination, args.width, args.grayscale)
        print(f"Saved: {destination}")
    elif args.input.is_dir():
        files = [p for p in args.input.iterdir()
                 if p.is_file() and p.suffix.lower() in SUPPORTED]
        for source in files:
            destination = output_name(source, args.output_dir)
            process_image(source, destination, args.width, args.grayscale)
            print(f"Saved: {destination}")
        print(f"Processed {len(files)} image(s).")
    else:
        parser.error("input must be an existing image file or folder")


if __name__ == "__main__":
    main()
