from einzztools import call
import json

status, data = call("user/userInfoHistory", secUid="MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM")
print(status)
print(json.dumps(data, indent=2)[:1600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "dates": [
      "2026-10-06",
      "2026-10-04",
      "2026-10-02",
      "2026-10-01",
      "2026-09-30",
      "2026-09-28",
      "2026-09-27",
      "2026-09-25",
      "2026-09-21",
      "2026-09-20",
      "2026-09-19",
      "2026-09-17",
      "2026-09-14",
      "2026-09-12",
      "2026-09-07",
      "2026-09-03",
      "2026-08-31",
      "2026-08-30",
      "2026-08-22",
      "2026-08-19",
      "2026-08-18",
      "2026-08-16"
    ]
  },
  "continuationToken": "cont_eyJwdXJwb3NlIaoidXNlckluZm9IagN0b3J5Iiwic2VjVWlkIjoiTVM0d0xqQUJBQUFBc05tb"
}
"""
