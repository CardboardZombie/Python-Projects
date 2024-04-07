import unittest
from unittest.mock import patch, MagicMock
from create_images_from_repo import get_images_from_web, download_images


class TestImageDownload(unittest.TestCase):
    @patch('create_images_from_repo.get_digimon_data')
    @patch('create_images_from_repo.download_images')
    def test_valid_image_url(self, mock_download_images, mock_get_digimon_data):
        # Mocking Digimon API response with a valid image URL
        mock_get_digimon_data.return_value = {
            'name': 'Agumon',
            'images': [{'href': 'https://digimon-api.com/images/digimon/w/Agumon.png'}]
        }

        # Calling the function under test
        get_images_from_web(
            {
                'actions': {'download_images_from_web': True, 'create_all_images': False},
                'target_ids': {'product_codes': ['289']},
                'utilities': {'downloads_folder': 'downloaded_images'}
            }
        )

        # Asserting that download_images function was called with the correct arguments
        mock_download_images.assert_called_once_with(
            {'289': ['Agumon', 'https://digimon-api.com/images/digimon/w/Agumon.png']}, 'downloaded_images'
        )

    @patch('create_images_from_repo.get_digimon_data')
    @patch('create_images_from_repo.download_images')
    def test_invalid_image_url(self, mock_download_images, mock_get_digimon_data):
        # Mocking Digimon API response with an invalid image URL
        mock_get_digimon_data.return_value = {
            'name': 'Agumon',
            'id': '289',
            'images': [{'href': 'invalid_url'}]
        }

        # Calling the function under test
        get_images_from_web(
            {
                'actions': {'download_images_from_web': True, 'create_all_images': False},
                'target_ids': {'product_codes': ['289']},
                'utilities': {'downloads_folder': 'downloaded_images'}
            }
        )

        # Asserting that download_images function was not called
        mock_download_images.assert_not_called()

    @patch('create_images_from_repo.get_digimon_data')
    @patch('create_images_from_repo.download_images')
    def test_broken_image(self, mock_download_images, mock_get_digimon_data):
        # Mocking Digimon API response with a broken image URL
        mock_get_digimon_data.return_value = {
            'name': 'Agumon',
            'images': [{'href': 'https://digimon-api.com'}]
        }

        # Mocking download_images function to raise an exception when called
        mock_download_images.side_effect = Exception("Image download failed")

        # Calling the function under test
        get_images_from_web(
            {
                'actions': {'download_images_from_web': True, 'create_all_images': False},
                'target_ids': {'product_codes': ['289']},
                'utilities': {'downloads_folder': 'downloaded_images'}
            }
        )

        # Asserting that download_images function was called
        mock_download_images.assert_called_once_with(
            {'Agumon': ['Agumon', 'https://digimon-api.com']}, 'downloads_folder'
        )


if __name__ == '__main__':
    unittest.main()
