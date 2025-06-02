from PIL import Image

def convert_image_format(input_path: str, output_name: str, target_format: str) -> str:
    """
    Convert an image to the specified format.
    
    Args:
        input_path: Path to the input image
        output_name: Name for the output file (without extension)
        target_format: Target format (e.g., 'webp', 'png', 'jpg')
        
    Returns:
        str: Path to the converted image
    """
    img = Image.open(input_path)
    output_path = f"{output_name}.{target_format}"
    img.save(output_path)
    return output_path 