# EinzzTools Site - https://einzzcookie.org/
TikTok Osint Website - Developed by EinzzCookie and https://einzzcookie.org/credits </br></br>
A robust, high-performance unofficial TikTok API wrapper designed for seamless automation, data extraction, and custom scripting. 
Built by reverse-engineering internal TikTok API structure and endpoints, this library delegates complex security challenges and signature handling to a dedicated server connection. 
Whether you are building private scripts, analytical dashboards, or automated workflows, this wrapper simplifies interaction with TikTok's data pipeline with minimal setup.

![fmhy](https://cdn.jsdelivr.net/gh/JMcrafter26/badges@main/src/assets/available/fmhy/cozy.svg)
## API
EinzzTools API <- https://einzzcookie.org/api

Base URL: `https://einzzcookie.org/v1/`

### Authentication
Every request needs two headers. Both must belong together, and the key must be active. Always send them as headers, never in the URL.

```text
X-Email: the email you logged in with
X-API-Key: einzztools-xxxxxxxxxxxxxxxxxxxxx
```

### Quick start
```python
from einzztools import call
import json

status, data = call("video/info", url="https://vm.tiktok.com/ZN8rL25vx/")
print(status)
print(json.dumps(data, indent=2)[:1000])
```

### Rate limit
* Optional: To get the limit data of your API key:

```python
  import einzztools
  print(einzztools.last_rate_limit)
```

  which returns for example:

```json
  {"limit": 2500, "remaining": 2438, "reset_seconds": 30140}
```

The counter resets every day at 00:00 UTC. Requests above the limit are still counted. At 110% of your daily limit the key is blocked and you have to contact @EinzzCookie on Telegram.

### TikTok session ID (private content)
For your own private account, videos or stories you can send your TikTok `sessionid` in the header `X-Session-Id`, together with your API key headers. It works on: `user/userInfo`, `user/userLikes`, `user/userStory`, `user/userReposts`, `video/info`, `video/infoBatch`, `video/videoComments` and `video/videoDownloader`.

```python
from einzztools import call

status, data = call(
    "video/info",
    url="https://vm.tiktok.com/ZN8rL25vx/",
    session_id="your_tiktok_sessionid",   # sent as X-Session-Id header, not in the URL
)
```

```bash
curl 'https://einzzcookie.org/v1/video/videoDownloader?url=https://vm.tiktok.com/xxxx' \
  -H 'X-Email: you@example.com' \
  -H 'X-API-Key: einzztools-xxxxxxxxxxxxxxxxxxxxx' \
  -H 'X-Session-Id: your_tiktok_sessionid'
```

* Always use the header, never the URL. It must be 16-128 letters/digits, otherwise the API answers `400 Invalid sessionid format`.
* The session ID is only sent to TikTok and is never logged or stored (the history only records that one was used).
* Responses made with a session ID are not cacheable (`Cache-Control: no-store`).
* The session ID and the API key are two different things: the key is for this API, the session ID is your TikTok login.
* Download links in responses (`proxyUrl`, `proxyUrls`) point to `/v1/...`. Fetch them with the same `X-Email` / `X-API-Key` headers, plus `X-Session-Id` for private posts. Each fetch counts as one request.
* For more informations about session ID check out https://einzzcookie.org/sessionid

### Request codes
Every authenticated request gets a unique random request code like `req_K7M2XQ9TBHA4NVCW5R3D`. No code is ever issued twice. It is returned:

* in the JSON body as `requestCode` (together with `historySaved`)
* in the response headers `X-Request-Code` and `X-History-Saved` (also on media downloads)

Requests with a wrong email or key get no code.

```python
status, data = call("user/userInfo", username="tiktok")
print(data["requestCode"], data["historySaved"])
```

### API history
By default every request is saved to your history: your account, the method, the path, the query, the result status and the duration.

**Choose per request whether it is saved** with the header `X-Save-History: false` or the parameter `saveHistory=false` (values: `true` / `false`, default `true`):

```python
status, data = call("user/userInfo", username="tiktok", save_history=False)  # sends X-Save-History: false
```

```bash
curl 'https://einzzcookie.org/v1/user/userInfo?username=tiktok&saveHistory=false' \
  -H 'X-Email: you@example.com' \
  -H 'X-API-Key: einzztools-xxxxxxxxxxxxxxxxxxxxx'
```

If a request is not saved, only its code and the time are kept, nothing about you or the request. An invalid value returns `400`.

**Read your history** with `GET /v1/history` (newest first):

```python
status, data = call("history", limit=25)              # limit 1-100, default 50
for e in data["data"]["entries"]:
    print(e["code"], e["createdAt"], e["method"], e["path"], e["query"], e["status"])

nxt = data["data"]["next"]                            # None when there is no more
if nxt:
    status, more = call("history", limit=25, before=nxt)

status, one = call("history", code="req_K7M2XQ9TBHA4NVCW5R3D")   # one specific request
```

* Only saved requests appear. Reading the history is not saved itself, but counts as one request towards your daily limit.
* Secrets are never stored: any query parameter whose name contains `session`, `key`, `token` or `secret` is stored as `[redacted]`.
* The same list is shown on https://einzzcookie.org/api in the "Request history" box.

### Response codes
| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad parameter, invalid session ID format, or invalid `saveHistory` value |
| 401 / 403 | Missing headers, email and key do not match, or the subscription is not active |
| 403 | The key is blocked (contact @EinzzCookie on Telegram) |
| 404 | Your authentication is correct, however your API path is wrong |
| 429 | Daily limit reached, try again after 00:00 UTC (see the `Retry-After` header) |

## Project Structure
```text
EinzzTools-main/
├── other/         # Utility functions (QR codes, link checker, fake sharing)
├── user/          # User-centric modules (info, history, likes, reposts, sharing analyse, stories)
├── video/         # Video-centric modules (downloader, comments, info, sharing analyse)
├── LICENSE        # Project license
└── README.md      # Documentation
```

#### URL

##### General Pages
* Homepage <- https://einzzcookie.org/
* Blog <- https://einzzcookie.org/blog
* Credits <- https://einzzcookie.org/credits
* Donations <- https://einzzcookie.org/donate

##### Tool Pages
###### User Tools
* User Info <- https://einzzcookie.org/user / https://einzzcookie.org/ 
* User Story <- https://einzzcookie.org/story
* User Monitoring <- https://einzzcookie.org/monitor
* User Reposts <- https://einzzcookie.org/reposts
* User Shared <- https://einzzcookie.org/user-shared
* User Shared Private <- https://einzzcookie.org/user-shared-private

###### Video Tools
* Video Info <- https://einzzcookie.org/video
* Video Comments <- https://einzzcookie.org/comments
* Video Downloader <- https://einzzcookie.org/download
* Video Shared <- https://einzzcookie.org/video-shared
* Video Shared Private <- https://einzzcookie.org/video-shared-private

###### Special Tools
* Share Anonymously <- https://einzzcookie.org/share
* User QR-Code <- https://einzzcookie.org/qrcode
* Link Checker <- https://einzzcookie.org/link-checker

###### Law Pages
* ToS <- https://einzzcookie.org/tos
* Privacy <- https://einzzcookie.org/privacy
* Impressum <- https://einzzcookie.org/impressum

## Co-Info
We reserve the right to modify, suspend, or terminate API keys, access tiers, request limits, and pricing plans at any time without prior notice. The API is provided on an "as-is" and "as-available" basis with no uptime guarantees. While we strive for continuous availability and accurate data collection, we make no warranties-express or implied-regarding the accuracy, completeness, or reliability of the data returned by the service.

## Dead-Man Switch
In the event that the lead developer (@EinzzCookie) is no longer able to maintain this project, an automated 3-month countdown is active after every update. If no update is pushed within 90 days, the complete EinzzTools source code, setup guide, and documentation will be automatically released publicly to the community-with the hope that others will honor the project's legacy and continue its development.
