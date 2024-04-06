import requests
import os
import time
import configparser


def configure_data():
    # Create a configparser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Extract data from the configuration file
    config_data = {
        'actions': {
            'download_images_from_web': config.getboolean('actions', 'download_images_from_web'),
            'create_all_images': config.getboolean('actions', 'create_all_images')
        },
        'utilities': {
            'height_padding': config.getint('utilities', 'height_padding'),
            'width_padding': config.getint('utilities', 'width_padding'),
            'resize_images_to': config.get('utilities', 'resize_images_to'),
            'output_folder': config.get('utilities', 'output_folder')
        },
        'exceptions': {
            'exceptions': config.get('en_name_exceptions', 'digimon_translations')
        },
        'target_ids': {
            'product_codes': config.get('digimon_ids', 'digidestined_partners').split(", "),
            'max_id': config.getint('digimon_ids', 'max_digimon_id')
        }
    }

    # Return the extracted configuration data
    return config_data


def get_start_time():
    return time.perf_counter()


def get_time_taken(start_time):
    elapsed_time = time.perf_counter() - start_time
    print(format_elapsed_time(elapsed_time))


def format_elapsed_time(elapsed_time):
    """
    Format elapsed time into a human-readable string.

    Args:
        elapsed_time (float): Elapsed time in seconds.

    Returns:
        str: Formatted string representing elapsed time.
    """
    if elapsed_time < 1:
        return f"Elapsed time: {elapsed_time:.2f} seconds"
    elif elapsed_time < 60:
        return f"Elapsed time: {elapsed_time:.0f} seconds"
    elif elapsed_time < 3600:
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        return f"Elapsed time: {minutes:02d}:{seconds:02d}"
    else:
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        return f"Elapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}"

    # Iterate through the image URLs dictionary
    count = 0
    for identifier, url in image_urls_dict.items():
        try:
            # Send a GET request to the image URL
            response = requests.get(url)
            if response.status_code == 200:
                # Extract the filename from the URL
                filename = os.path.join(output_directory, f"{identifier}.png")

                # Save the image to the output directory
                with open(filename, 'wb') as f:
                    f.write(response.content)

                count += 1
            else:
                print(f"Failed to download image for {identifier}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image for {identifier}: {e}")

    print(f"{count} images downloaded successfully.")


def download_images(image_urls_dict, output_directory):
    """
    Download images from a dictionary of image URLs.

    Args:
        image_urls_dict (dict): Dictionary of image URLs where keys are identifiers and values are URLs.
        output_directory (str): Directory where the downloaded images will be saved.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through the image URLs dictionary
    count = 0
    for identifier, row in image_urls_dict.items():
        url = row[1]
        try:
            # Send a GET request to the image URL
            response = requests.get(url)
            if response.status_code == 200:
                # Extract the filename from the URL
                filename = os.path.join(output_directory, f"{identifier}.png")

                # Save the image to the output directory
                with open(filename, 'wb') as f:
                    f.write(response.content)

                count += 1
            else:
                print(f"Failed to download image for {identifier}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image for {identifier}: {e}")

    print(f"{count} images downloaded successfully.")