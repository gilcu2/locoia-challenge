from urllib.parse import urlencode
import requests
from pydantic import BaseModel


class GistFile(BaseModel):
    filename: str
    raw_url: str
    size: int
    text: str


class Gist(BaseModel):
    url: str
    files: list[GistFile]


def get_gists(
        username: str | None = None, page: int | None = None, per_page: int | None = None
) -> list[Gist]:
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
        gists_url += "?" + urlencode(params)

    response = requests.get(gists_url)
    result = response.json()
    gists = []
    for r in result:
        files = []
        for filename in r["files"]:
            file_dict = r["files"][filename]
            files.append(GistFile(
                filename=filename,
                raw_url=file_dict["raw_url"],
                size=file_dict["size"],
                text=file_dict["text"]
            ))
        gists.append(Gist(url=r["url"], files=files))
    return gists


def download_whole_file(file: GistFile) -> GistFile:
    response = requests.get(file.url)
    file.text = response.text
    return file
