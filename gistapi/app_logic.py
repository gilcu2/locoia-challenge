def extract_matches(gists, pattern: str, username: str) -> dict[str, str]:
    matches = []
    for gist in gists:
        matches.append(gist)

    return {'status': 'success', 'username': username, 'pattern': pattern, 'matches': matches}
