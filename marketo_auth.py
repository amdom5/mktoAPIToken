import requests
from datetime import datetime, timedelta

def get_marketo_token(identity_url, client_id, client_secret):
    """
    Get Marketo access token using client credentials.

    Args:
    - identity_url (str): Marketo Identity URL.
    - client_id (str): Client ID for authentication.
    - client_secret (str): Client Secret for authentication.

    Returns:
    - str: Access token for subsequent API calls.
    """

    token_url = f"{identity_url}/oauth/token"
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_url, params=params)
    response_data = response.json()

    if 'access_token' in response_data:
        return response_data['access_token']
    else:
        raise Exception(f"Failed to retrieve access token. Error: {response_data}")

def is_token_valid(access_token, token_expiration):
    """
    Check if the access token is still valid based on its expiration time.

    Args:
    - access_token (str): Access token for authentication.
    - token_expiration (int): Expiration time of the access token in seconds.

    Returns:
    - bool: True if the token is still valid, False otherwise.
    """

    headers = {'Authorization': f'Bearer {access_token}'}
    validation_url = "https://<your_marketo_api_url>/rest/v1/leads.json"  # Use a valid API endpoint for validation

    response = requests.get(validation_url, headers=headers)
    
    if response.status_code == 200:
        return True
    elif response.status_code == 601:  # Invalid token error code
        return False
    else:
        raise Exception(f"Error validating access token. Status Code: {response.status_code}")

# Example Usage:
# Replace 'your_identity_url', 'your_client_id', 'your_client_secret', 'your_marketo_api_url' with your actual values.
identity_url = 'your_identity_url'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
token_expiration = 3600  # Assuming the token lifespan is 3600 seconds

access_token = get_marketo_token(identity_url, client_id, client_secret)

if is_token_valid(access_token, token_expiration):
    print("Token is valid. Proceed with API calls.")
else:
    print("Token expired or invalid. Renew the token.")
