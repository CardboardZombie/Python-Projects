# Digimon Image Downloader

The Digimon Image Downloader is a Python script that allows users to download images of Digimon characters from a web API and process them according to specified configurations.


## Table of Contents
Overview

Installation

Usage

Configuration

Contributing

Output

## Overview
The Digimon Image Downloader project consists of Python scripts designed to interact with a Digimon API to download images of Digimon characters. It also provides functionality to process these images, such as resizing and pasting them onto templates.

## Installation
To use the Digimon Image Downloader, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/your-username/digimon-image-downloader.git
2. Navigate to the project directory:

cd digimon-image-downloader
3. Install the required dependencies:

pip install -r requirements.txt

## Usage
To use the Digimon Image Downloader, you can run the create_images_from_repo.py script:

python create_images_from_repo.py

This will execute the script and download images from the Digimon API, process them, and save the processed images to an output directory.

## Configuration
The Digimon Image Downloader uses a configuration file (config.ini) to specify various settings, such as actions to perform, utility parameters, and Digimon IDs. You can modify this configuration file to customize the behavior of the script.

Here's an example of the config.ini file:

ini
Copy code
[actions]
download_images_from_web=yes
create_all_images=yes

[utilities]
height_padding=323
width_padding=323
max_height=247
max_width=247
downloads_folder=downloaded_images
output_folder=output

[digimon_ids]
digidestined_partners = 289, 394, 991, 114, 346, 669, 412, 878
max_digimon_id = 1471
You can customize the settings in this file according to your requirements.

## Contributing
Contributions to the Digimon Image Downloader project are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Make your changes and commit them: git commit -am 'Add new feature'.
Push to your branch: git push origin feature-name.
Submit a pull request.

## Output
Getting the images from the target websites through API...
...
1456 images downloaded successfully.
1456 images processed.
Elapsed time: 05:47
