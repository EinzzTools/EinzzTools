from einzztools import call
import json

status, data = call("other/shareFake",
                    videoUrl="https://www.tiktok.com/@tiktok/video/1231231123")
print(status)
print(json.dumps(data, indent=2))

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "link": "https://vt.tiktok.com/ZS9UjEQrbx5UV-btjMX/"
  }
}
"""
