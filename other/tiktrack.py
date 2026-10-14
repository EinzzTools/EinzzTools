# tiktrack.py
import json
import urllib.request
import urllib.error
import urllib.parse

EMAIL = "cookie@gmail.com"
KEY = "tiktrack-#####################"
BASE = "https://einzzcookie.org/v1/"


def call(path, **params):
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(
        f"{BASE}{path}?{query}",
        headers={"X-Email": EMAIL, "X-API-Key": KEY},
    )
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")
