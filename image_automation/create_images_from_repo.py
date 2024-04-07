from digimon_api import get_digimon_data
from utils import (
    download_images, get_time_taken, configure_data, get_start_time, extract_product_codes, generate_number_list
)
from image_processing import process_images


def get_images_from_web(config):
    print('Getting the images from the target websites through API...')
    url_data = {}
    if config['actions']['create_all_images']:
        config['target_ids']['product_codes'] = generate_number_list(config['target_ids']['max_id'])
    product_identifiers = config['target_ids']['product_codes']
    # print(product_identifiers)
    # Fetch data for each Digimon ID or name and print it
    for identifier in product_identifiers:
        target_data = get_digimon_data(identifier)
        if target_data:
            # print(f"Image URL for {target_data['name']}: {target_data['images'][0]['href']}")
            # target_url = target_data['images'][0]['href'].replace('(', '%28').replace(')', '%29')
            url_data[identifier] = [target_data['name'], target_data['images'][0]['href']]

    # Output directory where the downloaded images will be saved
    output_directory = config['utilities']['downloads_folder']

    # Download the images
    download_images(url_data, output_directory)


def create_all_images(config):
    # config['target_ids']['product_codes'] = list(range(1, config['target_ids']['max_id'] + 1))
    output_directory = config['utilities']['downloads_folder']
    config['target_ids']['product_codes'] = extract_product_codes(output_directory)
    return config


def main():
    # Record the starting time
    start_time = get_start_time()
    ###############################################
    # Define a dictionary to map configuration keys to corresponding actions or functions
    action_mapping = {
        'download_images_from_web': lambda: get_images_from_web(config),
        'create_all_images': lambda: create_all_images(config),
    }
    # configure the customizable inputs for the script to run as intended
    config = configure_data()
    action_script = config['actions']

    # Iterate through each key in action_script and execute the corresponding action if the value is True
    for key, action in action_mapping.items():
        if action_script.get(key, False):
            action()

    # Execute the primary action when running this script.
    print(f"Creating fresh images from {config['target_ids']['product_codes']}...")
    process_images(config['target_ids']['product_codes'], config['utilities'])
    ###############################################
    # Calculate the elapsed time
    get_time_taken(start_time)


if __name__ == "__main__":
    main()
