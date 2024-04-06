import requests


def get_digimon_data(digimon_identifier):
    # Define the URL of the Digimon API
    url = f'https://digi-api.com/api/v1/digimon/{digimon_identifier}'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and return the JSON data
        return response.json()
    else:
        # If the request failed, print an error message
        print(f"Failed to fetch data for Digimon with identifier {digimon_identifier}")
        return None
