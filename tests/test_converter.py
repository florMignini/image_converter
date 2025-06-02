import sys
import os
import pytest
from io import BytesIO
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_converter.converter import convert_image_format

@pytest.fixture
def test_image_path(tmp_path):
    # create a 100x100 red image and save it in tmp_path
    img = Image.new("RGB", (100, 100), color="red")
    img_path = tmp_path / "test_image.jpg"
    img.save(img_path)
    return str(img_path)

def test_convert_image_format(test_image_path):
    output_filename = "resultado"
    output_format = "png"

    output_path = convert_image_format(test_image_path, output_filename, output_format)

    assert os.path.exists(output_path), "No se creó el archivo convertido"
    assert output_path.endswith(f".{output_format}"), f"La extensión esperada era '.{output_format}'"

    # optional: delete the created file after the test
    os.remove(output_path)
