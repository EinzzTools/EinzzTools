from tiktrack import call
import json

status, data = call("video/videoDownloader",
                    url="https://www.tiktok.com/@tiktok/video/1231231231231")
print(status)
print(json.dumps(data, indent=2)[:1600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "success": true,
    "videoId": "123123123131",
    "videoUrl": "https://www.tiktok.com/video/123123131231",
    "downloadUrl": "https://v16m-default.tiktokcdn-us.com/df92cc312334625869e7270123162d0cf51d60/6ad05430f90/video/tos/useast5/tos-u5seast5-ve-0068c05503-tx/oYjIxXiCJC8y5V9pxCsN8h5GwIBfAgs8iB5QAwAF1sE/?a=1&bti=OHYpOTYsfdsd0Zik3OjlmOm01MzE6sdfZDQ0MDo%3D&&bt=710&ft=8TwrxU2sfusfdsQOFC5sdfrSfvgFLO-XtQi00wQEe-InzAT.YqAsdfnnbvWH6&mime_type=video_mp4&rc=aTw1ZasdTllOTk0aDU2ZGg3NkBpajasdM6ZWs5cnhyZDMzZzczN12fEA2NDM2NF4zNgTExNS5gNGMzhSNlLS5yMmRjYXJhfsaLS1kMS9zcw%3D%3asD&vvpl=1&l=20261011244172as1254207A60512408DF3B931BFCEB&btag=e000bdf18000",
    "title": "Tiktok News",
    "author": "tiktok",
    "stats": {
      "views": 18011866,
      "likes": 9582,
      "comments": 16202,
      "shares": 851
    },
    "duration": 214,
    "timestamp": "2022-10-14T19:25:45.296Z"
  }
}
"""