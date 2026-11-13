# einzztools.py
import json
import urllib.request
import urllib.error
import urllib.parse

EMAIL = "cookie@gmail.com"
KEY = "einzztools-#####################"
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


def _send(req):
    global last_rate_limit
    try:
        with urllib.request.urlopen(req) as r:
            last_rate_limit = _read_limits(r.headers)
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        last_rate_limit = _read_limits(e.headers)
        return e.code, json.loads(e.read().decode() or "{}")


def call(path, session_id=None, save_history=True, **params):
    """session_id: your TikTok sessionid (sent as X-Session-Id header, never in the URL).
    save_history: False sends X-Save-History: false. The response contains requestCode."""
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(
        f"{BASE}{path}?{query}",
        headers={
            "X-Email": EMAIL,
            "X-API-Key": KEY,
            "X-Save-History": "true" if save_history else "false",
            **({"X-Session-Id": session_id} if session_id else {}),
        },
    )
    return _send(req)


def delete_history(all=False, from_time=None, to_time=None, last=None, code=None):
    """Deletes saved history. Use exactly ONE of:
      all=True                      the entire history
      from_time=... / to_time=...   a time range (ISO 8601 string, epoch seconds/ms or datetime; one may be omitted)
      last=10                       the 10 most recently logged requests
      code="req_..."                one specific request
    Returns (status, data); data["data"]["deleted"] is the number of removed entries."""

    def ts(v):
        if v is None or isinstance(v, (str, int)):
            return v
        if hasattr(v, "isoformat"):
            if v.tzinfo is None:
                return v.isoformat() + "Z"
            return v.isoformat()
        raise TypeError("timestamp must be str, int or datetime")

    params = {
        "all": "true" if all else None,
        "from": ts(from_time),
        "to": ts(to_time),
        "last": last,
        "code": code,
    }
    chosen = [
        all,
        from_time is not None or to_time is not None,
        last is not None,
        code is not None,
    ]
    if sum(bool(c) for c in chosen) != 1:
        raise ValueError("Use exactly one of: all, from_time/to_time, last, code")

    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(
        f"{BASE}history?{query}",
        method="DELETE",
        headers={"X-Email": EMAIL, "X-API-Key": KEY},
    )
    return _send(req)
