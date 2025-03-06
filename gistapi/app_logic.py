import re
from gistapi.github_calls import Gist
from pydantic import BaseModel


class GistResult(BaseModel)
    status: str
    username: str
    pattern: str
    matches: list[Gist]
    total: int


def filter(gists: list[Gist], pattern: str) -> list[Gist]:
    matches = []
    for gist in gists:
        file_matches = [file for file in gist.files if re.match(pattern, file.text)]
        if len(file_matches) > 0:
            gist.files = file_matches
            matches.append(gist)

    return matches


def create_result(
        gists: list[Gist], filtered_gists: list[Gist], pattern: str, username: str
) -> GistResult:
    return GistResult(
        status="success",
        username=username,
        pattern=pattern,
        matches=filtered_gists,
        total=len(gists),
    )
