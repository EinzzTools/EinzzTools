from einzztools import call
import json

status, data = call("user/userInfo", username="tiktok")
print(status)
print(json.dumps(data, indent=2)[:6600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
    "username": "tiktok",
    "nickname": "TikTok",
    "userId": "107955",
    "signature": "Your next discovery is waiting on TikTok.",
    "createTime": "2015-02-28T17:22:29.000Z",
    "avatarLarger": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=00e43db7&x-expires=1792170000&x-signature=elIDd%2Ft2qSPdOUrtnpjNjOENCmw%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=no1a",
    "region": null,
    "regionName": null,
    "regionFlag": null,
    "locked_region": null,
    "locked_regionName": null,
    "locked_regionFlag": null,
    "language": "en",
    "isVerified": true,
    "isPrivate": false,
    "isBusiness": false,
    "isMuted": false,
    "bioLink": "tiktok.com/discovermore",
    "isEmbedBanned": false,
    "ttSeller": false,
    "openFavorite": false,
    "followingVisibility": 1,
    "nickNameModifyTime": "2021-12-03T19:26:40.000Z",
    "followerCount": 96240045,
    "followingCount": 1,
    "heart": 464784242,
    "videoCount": 1498,
    "totalVideoCount": 1991,
    "hiddenVideoCount": 493,
    "friendCount": 7,
    "storyTotalCount": 0,
    "lastStoryCreatedAt": null
  },
  "video_data": [
    {
      "id": "7694797676306615583",
      "desc": "this summer gave us pop songs, glam routines, and a few main-character habits. @McCall Mirabella breaks down this summer's souvenirs \ud83d\udc2c\u2600\ufe0f",
      "height": 1280,
      "width": 720,
      "ratio": "720p",
      "coverUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast8-p-0068-tx2/osDEKIayAATxid4XIifhL1BBXAZ8wiCZcATiAJ~tplv-tiktokx-origin.image?dr=10395&x-expires=1792170000&x-signature=kAKqYSIYZp0KLu5oCMEGWm%2FkwXA%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
      "originCoverUrl": "https://p19-common-sign.tiktokcdn-eu.com/tos-useast8-p-0068-tx2/oIiSKVaoIVstALfejHqglAI03jokC4GlIg5ejX~tplv-tiktokx-origin.image?dr=10395&x-expires=1792170000&x-signature=yZmFvvzdprRLaO6eH0TcVL1Ml0c%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
      "dynamicCoverUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast8-p-0068-tx2/osDEKIayAATxid4XIifhL1BBXAZ8wiCZcATiAJ~tplv-tiktokx-origin.image?dr=10395&x-expires=1792170000&x-signature=kAKqYSIYZp0KLu5oCMEGWm%2FkwXA%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
      "playAddr": "https://v45.tiktokcdn-eu.com/e94a86a0aac4f2eba8eef3c3c93c5deb/6ad25970/video/tos/alisg/tos-alisg-ve-37c799-sg/ogJEilqISNrDaBR0ARVeWfEVFEAR2gyyu8R0TQ/?a=1233&bti=ODszNWYuMDE6&&bt=1603&ft=_sd5EP0pC12NvjpxFF7nRfqWvlcI6IxVvYqpiX&mime_type=video_mp4&rc=M2czaWg1Ozo7ODVpNjkzOEBpM281NHM5cm5wZTMzaTczNEBjYmItYTU0XzUxLTI2YGI1YSNzZWlhMmRjZjFhLS1kMTJzcw%3D%3D&vvpl=1&l=2026101417050205D235B92019913FFF79&btag=e0008d000&sp_exp=hash_v0",
      "playCount": 762300,
      "privateItem": false,
      "authorUniqueId": "tiktok"
    }
}
"""
