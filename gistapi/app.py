"""
Exposes a simple HTTP API to search a users Gists via a regular expression.

GitHub provides the Gist service as a pastebin analog for sharing code and
other development artifacts.  See http://gist.github.com for details.  This
module implements a Flask server exposing two endpoints: a simple ping
endpoint to verify the server is up and responding and a search endpoint
providing a search across all public Gists for a given GitHub account.
"""

from flask import Flask, jsonify, request, abort
from gistapi.github_calls import get_gists
from gistapi.app_logic import filter, create_result
import logging, sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] "
    "[%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/api/v1/search", methods=['POST'])
def search():
    """Provides matches for a single pattern across a single users gists.

    Pulls down a list of all gists for a given user and then searches
    each gist for a given regular expression.

    Returns:
        A Flask Response object of type application/json.  The result
        object contains the list of matches along with a 'status' key
        indicating any failure conditions.
    """
    post_data = request.get_json()

    username = post_data.get('username')
    pattern = post_data.get('pattern', '.*')
    page = post_data.get('page')
    per_page = post_data.get('per_page')

    try:
        gists = get_gists(username, page, per_page)

        filtered = filter(gists, pattern)
        result = create_result(gists, filtered, pattern, username)

        return jsonify(result)
    except Exception as e:
        err = f"Problem getting gists from github for user {username}: {e}"
        logger.exception(err)
        abort(500, description=err)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9876)
