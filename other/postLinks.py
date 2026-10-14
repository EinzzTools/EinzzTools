from tiktrack import call
import json

status, data = call("other/postLinks", url="https://tiktok.com")
print(status)
print(json.dumps(data, indent=2))


# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "risk": 0,
    "riskLevel": "Trusted",
    "riskEmoji": "\u2705"
  }
}
"""