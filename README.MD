# image_converter

A simple and efficient Python image format converter using Pillow.

---

## Description

This project allows you to convert images between common formats (JPEG, PNG, etc.) easily and efficiently. Great for automation scripts, batch processing, or integration into other projects.

---

## Features

- Convert common image formats.
- Supports file streams to minimize disk I/O.
- Modular, well-tested code using `unittest` and `pytest`.
- Easy to integrate with other Python projects.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/florMignini/image_converter.git
cd image_converter
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Basic usage
Basic example to convert a JPG image to PNG:
```python
from image_converter.converter import convert_image_format

output_file = convert_image_format("input.jpg", "output_image", "png")
print(f"Converted image saved as {output_file}")

```

## Running tests
Run tests using pytest:
```bash
pytest
```
Run using unittest:
```bash
python3 -m unittest discover tests
```

## Contributing

Feel free to submit issues and enhancement requests!

## License
MIT License © Florencia Mignini

## Contact
Florencia Mignini - flormignini29@.com
GitHub: https://github.com/florMignini

```css

If you want, I can generate the file content for you to copy or save directly. Want me to do that?
```