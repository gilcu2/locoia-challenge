from urllib.parse import urlencode

import requests
from pydantic import BaseModel


class GistFile(BaseModel):
    filename: str
    url: str|None = None
    size: int
    text: str | None = None


class Gist(BaseModel):
    url: str
    files: list[GistFile]


def get_gists(
        username: str | None = None, page: int | None = None, per_page: int | None = None,
        maximun_size: int | None = None, minimun_size: int | None = None,
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

            if maximun_size and file_dict["size"] > maximun_size:
                continue
            if minimun_size and file_dict["size"] < minimun_size:
                continue

            if "content" in file_dict and not file_dict["truncated"]:
                text = file_dict["content"]
                url = None

            else:
                text = None
                url = None
                if "raw_url" in file_dict:
                    url = file_dict["raw_url"]
                elif "git_pull_url" in file_dict:
                    url = file_dict["git_pull_url"]

            files.append(GistFile(
                filename=filename,
                url=url,
                size=file_dict["size"],
                text=text
            ))
        if len(files) > 0:
            gists.append(Gist(url=r["url"], files=files))
    return gists


def download_file(url: str) -> str:
    response = requests.get(url)
    return response.text
