# einzztools.py
import json
import urllib.request
import urllib.error
import urllib.parse

EMAIL = "#########@gmail.com"
KEY = "tiktrack-#####################"
BASE = "https://einzzcookie.org/v1/"

last_rate_limit = {}

def _read_limits(headers):
    def num(name):
        v = headers.get(name)
        return int(v) if v is not None and v.isdigit() else None

    return {
        "limit": num("X-RateLimit-Limit"),
        "remaining": num("X-RateLimit-Remaining"),
        "reset_seconds": num("X-RateLimit-Reset"),
    }


def call(path, **params):
    global last_rate_limit
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(
        f"{BASE}{path}?{query}",
        headers={"X-Email": EMAIL, "X-API-Key": KEY},
    )
    try:
        with urllib.request.urlopen(req) as r:
            last_rate_limit = _read_limits(r.headers)
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        last_rate_limit = _read_limits(e.headers)
        return e.code, json.loads(e.read().decode() or "{}")
