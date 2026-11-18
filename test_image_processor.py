from pathlib import Path
from PIL import Image
from image_processor import process_image


def test_resize_preserves_aspect_ratio(tmp_path: Path):
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    Image.new("RGB", (100, 50), "red").save(source)

    process_image(source, destination, width=40)

    with Image.open(destination) as result:
        assert result.size == (40, 20)


def test_grayscale_conversion(tmp_path: Path):
    source = tmp_path / "source.png"
    destination = tmp_path / "gray.png"
    Image.new("RGB", (10, 10), "red").save(source)

    process_image(source, destination, grayscale=True)

    with Image.open(destination) as result:
        assert result.mode == "L"
