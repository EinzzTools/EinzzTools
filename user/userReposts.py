from tiktrack import call

status, data = call("user/userReposts", username="tiktok", cursor="0", count="30")
print(status)
d = data["data"]
print(len(d["reposts"]), "reposts, hasMore =", d["hasMore"], ", cursor =", d["cursor"])

# Example Output: 
"""
200
199 reposts, hasMore = False , cursor = 320
"""