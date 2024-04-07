from pathlib import Path
from PIL import Image
import shutil


def create_output_directory(output_path):
    """
    Create the output directory if it doesn't exist.

    Args:
        output_path (str): Path to the output directory.
    """
    Path(output_path).mkdir(parents=True, exist_ok=True)


def load_template(template_path):
    """
    Load a template image from the given path.
    If the file is not a JPEG, convert PNGs to JPEGs before loading.

    Args:
        template_path (str): Path to the template image file.

    Returns:
        Image: Loaded template image.
    """
    template_path = Path(template_path)  # Convert to Path object if it's not already

    # Check if the file is a JPEG
    if template_path.suffix.lower() in ['.jpeg', '.jpg']:
        return Image.open(template_path)

    # If the file is a PNG, convert it to JPEG
    elif template_path.suffix.lower() == '.png':
        # Load the PNG image
        image = Image.open(template_path)

        # Create a new JPEG file path by replacing the extension
        jpeg_path = template_path.with_suffix('.jpeg')

        # Convert and save the PNG image as JPEG
        image.convert('RGB').save(jpeg_path, 'JPEG')

        # Return the loaded JPEG image
        return Image.open(jpeg_path)

    else:
        raise ValueError("Unsupported image format. Only JPEG and PNG are supported.")


def load_image(image_path):
    """
    Load an image from the given path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Image: Loaded image.
    """
    try:
        image = Image.open(image_path).convert('RGBA')
    except FileNotFoundError:
        raise FileNotFoundError(f"No image located for {image_path.stem}.png not found")
    return image


def resize_logo(logo_image, max_width, max_height):
    """
    Resize the logo image to fit within the specified maximum width and height.

    Args:
        logo_image (Image): Logo image.
        max_width (int): Maximum width for the resized logo.
        max_height (int): Maximum height for the resized logo.

    Returns:
        Image: Resized logo image.
    """
    # Get the original dimensions of the logo
    width, height = logo_image.size

    # Calculate the aspect ratio
    aspect_ratio = width / height

    # Calculate the new dimensions based on the maximum width and height
    new_width = min(width, max_width)
    new_height = min(height, max_height)

    # Check if resizing is necessary
    if width > max_width or height > max_height:
        # If the aspect ratio of the logo is wider than the template, resize based on width
        if aspect_ratio > (max_width / max_height):
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        # If the aspect ratio of the logo is taller than the template, resize based on height
        else:
            new_width = int(max_height * aspect_ratio)
            new_height = max_height

    # Resize the logo using the calculated dimensions
    resized_logo = logo_image.resize((new_width, new_height), Image.LANCZOS)

    return resized_logo


def paste_logo_on_image(template, logo, x, y):
    """
    Paste the logo image ontop of the template image, at the specified coordinates

    Args:
        template (Image): Template Image.
        logo (Image): Logo Image.
        x (int): x coordinate.
        y (int): y coordinate.

        [323,323] - > [570,323]
        [323,570] - > [570,570]
    """
    template_width, template_height = template.size
    center_x = template_width // 2
    center_y = template_height // 2

    # Calculate the top-left corner coordinates for pasting the logo image.
    logo_width, logo_height = logo.size
    starting_x = center_x - logo_width // 2
    starting_y = center_y - logo_height // 2
    # print(starting_x, starting_y)

    # Paste the operator logo onto the template image
    template.paste(logo, (starting_x, starting_y), logo)


def process_images(product_codes, utilities_dict):
    """
    Process images based on the provided product code list, exception dictionary, and adjustment values.

    Args:
        product_codes (list): List of product codes.
        utilities_dict (dict): Dictionary of utility data for product codes.
    """
    height_adj = utilities_dict['height_padding']
    width_adj = utilities_dict['width_padding']
    output_dir = utilities_dict['output_folder']
    create_output_directory(output_dir)
    counter = 0
    template_dir = Path("template_input")
    product_code_dir = Path("downloaded_images")
    output_path = Path(output_dir)
    template_count = 0
    for template_path in template_dir.glob("*.jpeg"):
        template_count += 1
        template_name = template_path.stem
        # print(template_name)
        template = load_template(template_path)
        for product in product_codes:
            image_path = Path(f"{product_code_dir}/{product}.png")

            try:
                logo_image = load_image(image_path)
            except FileNotFoundError as e:
                print(e)
                continue
            logo_image = resize_logo(logo_image, utilities_dict['max_height'], utilities_dict['max_width'])
            logo_width, logo_height = logo_image.size
            x = int(width_adj - (logo_width / 2))
            y = int(height_adj - (logo_height / 2))

            output_image_path = output_path / f"{product}_{template_count}.jpg"
            paste_logo_on_image(template, logo_image, x, y)

            template.save(output_image_path, "JPEG")
            counter += 1

    print(f"{counter} images processed.")
