import requests


def get_gists(username: str) -> dict[str, str]:
    gists_url = f'https://api.github.com/users/{username}/gists'
    response = requests.get(gists_url)
    return response.json()
