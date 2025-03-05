import re


def filter(gists: list[dict[str, str]], pattern: str) -> dict[str, str]:
    matches = []
    for gist in gists:
        if re.match(pattern, gist['description']):
            matches.append(gist)

    return matches


def create_result(gists: dict[str, str], filtered_gists: dict[str, str], pattern: str, username: str):
    return {
        'status': 'success',
        'username': username,
        'pattern': pattern,
        'matches': filtered_gists,
        "total": len(gists),
    }
