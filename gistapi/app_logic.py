import re

from pydantic import BaseModel

from gistapi.github_calls import Gist, download_file


class GistResult(BaseModel):
    status: str
    username: str|None=None
    pattern: str|None=None
    matches: list[Gist]
    total: int


def download_and_filter(gists: list[Gist], pattern: str) -> list[Gist]:
    matches = []
    for gist in gists:
        file_matches = []
        for file in gist.files:
            if file.text:
                text = file.text
            elif file.url:
                text = download_file(file.url)
            else:
                text=""

            if re.match(pattern, text):
                file.text = text
                file_matches.append(file)

        if len(file_matches) > 0:
            gist.files = file_matches
            matches.append(gist)

    return matches


def create_result(
        gists: list[Gist], filtered_gists: list[Gist], pattern: str, username: str|None
) -> GistResult:
    return GistResult(
        status="success",
        username=username,
        pattern=pattern,
        matches=filtered_gists,
        total=len(gists),
    )
