from einzztools import call
import json

status, data = call("user/userShared", url="https://www.tiktok.com/@channelnewsasia?_r=1&_t=ZG-ha512m9aGu")
print(status)
print(json.dumps(data, indent=2))

# Example Output: 
"""
{
  "success": true,
  "data": {
    "sharedUserSecUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
    "sharerUserSecUid": "MS4wLjasdABAAAAvasfasdasuXDJGDvJkmH_vz1qkDZYo1apxasgasgzaxdBSeIuPiM",
    "utmMedium": "android",
    "utmSource": "copy",
    "timestamp": "2025-09-25T07:25:28.000Z",
    "sharedUsername": "test",
    "sharerUsername": "tiktok"
  }
}
"""
