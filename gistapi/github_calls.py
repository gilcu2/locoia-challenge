import urllib

import requests


def get_gists(
    username: str | None = None, page: int | None = None, per_page: int | None = None
) -> list[dict[str, str]]:
    gists_url = (
        f"https://api.github.com/users/{username}/gists"
        if username
        else "https://api.github.com/gists"
    )
    params = {}
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page

    if len(params) > 0:
        gists_url += "?" + urllib.parse.urlencode(params)

    response = requests.get(gists_url)
    return response.json()
