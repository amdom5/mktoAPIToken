# Marketo Authentication Script

This Python script provides functions for obtaining and validating Marketo access tokens using client credentials. It includes a function to request the token and another to check if the token is still valid.

## Functions

### `get_marketo_token(identity_url, client_id, client_secret)`

Obtains Marketo access token using client credentials.

#### Parameters:

- `identity_url` (str): Marketo Identity URL.
- `client_id` (str): Client ID for authentication.
- `client_secret` (str): Client Secret for authentication.

#### Returns:

- `str`: Access token for subsequent API calls.

### `is_token_valid(access_token, token_expiration)`

Checks if the access token is still valid based on its expiration time by making a sample API call.

#### Parameters:

- `access_token` (str): Access token for authentication.
- `token_expiration` (int): Expiration time of the access token in seconds.

#### Returns:

- `bool`: True if the token is still valid, False otherwise.

## Example Usage

```python
# Replace 'your_identity_url', 'your_client_id', 'your_client_secret', and 'your_marketo_api_url' with your actual values.
identity_url = 'your_identity_url'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
token_expiration = 3600  # Assuming the token lifespan is 3600 seconds

access_token = get_marketo_token(identity_url, client_id, client_secret)

if is_token_valid(access_token, token_expiration):
    print("Token is valid. Proceed with API calls.")
else:
    print("Token expired or invalid. Renew the token.")
```

#### Note:

- Adjust the token_expiration variable based on your actual token lifespan.
- Make sure to replace placeholder values with your actual Marketo Identity URL, Client ID, Client Secret, and a valid Marketo API endpoint for validation.
