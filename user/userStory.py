from einzztools import call
import json

status, data = call("user/userStory", username="tiktok")
print(status)
print(json.dumps(data, indent=2)[:600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "username": "tiktok",
    "userId": "1522354",
    "isPrivate": false,
    "storyTotalCount": 0,
    "hasStories": false,
    "message": "This user has no active stories right now.",
    "stories": []
  }
}
"""
