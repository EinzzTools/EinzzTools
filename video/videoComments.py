from tiktrack import call

status, data = call("video/videoComments",
                    url="https://www.tiktok.com/@cbsnews/video/7691452115373395214",
                    cursor="0")
print(status)
d = data["data"]
print(len(d["comments"]), "comments of", d["total"], ", hasMore =", d["hasMore"])

# Example Output: 
"""
200
24 comments of 16799 , hasMore = 1
"""