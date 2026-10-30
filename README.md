# EinzzTools Site - https://einzzcookie.org/
TikTok Osint Website - Developed by EinzzCookie and https://einzzcookie.org/credits </br></br>
A robust, high-performance unofficial TikTok API wrapper designed for seamless automation, data extraction, and custom scripting. 
Built by reverse-engineering internal TikTok API structure and endpoints, this library delegates complex security challenges and signature handling to a dedicated server connection. 
Whether you are building private scripts, analytical dashboards, or automated workflows, this wrapper simplifies interaction with TikTok's data pipeline with minimal setup.

![fmhy](https://cdn.jsdelivr.net/gh/JMcrafter26/badges@main/src/assets/available/fmhy/cozy.svg)
## API
EinzzTools API <- https://einzzcookie.org/api
* Optional: To get the limit data of your API key:

```python
  import einzztools
  print(einzztools.last_rate_limit)
```

  which returns for example:

```json
  {"limit": 2500, "remaining": 2438, "reset_seconds": 30140}
```

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
