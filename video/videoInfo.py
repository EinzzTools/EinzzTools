from tiktrack import call
import json

status, data = call("video/info", url="https://www.tiktok.com/@tiktok/video/123123123131")
print(status)
print(json.dumps(data, indent=2)[:4600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "id": "123123213123131",
    "desc": "Tiktok",
    "tags": "#update #news",
    "createTime": "2021-07-10T22:02:42.000Z",
    "location": "US",
    "labels": [
      "Social Issues",
      "Society",
      "Society"
    ],
    "video": {
      "width": 720,
      "height": 1280,
      "duration": 23,
      "cover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast5-p-0012368-tx/oktNIpj88BAwhs0RqsidfxBI1ACCwwAAYXIJfAdsfsdf9i~tplv-tiktokx-origin.image?dr=10395&x-expires=1792112370000&x-signature=56wpU97wslsdf5vNWvbqHSEcysCsiU%3D&t=4d52140474&ps=13740610&shp=813424f88b70&shcp=5145bbe6a9&idc=no1a",
      "dynamicCover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast5-p-001268-tx/o09PqLJsdfGIGqCeeR4hsdfAAeAzwuEe4BcDOIRHIAwA~tplv-tiktokx-origin.image?dr=10395&x-expires=1142792170000&x-signaturesdf=wGc%2sdfBzmDTtFI2wFfShHSVWIQC1D4%3D&t=4d5b1240474&ps=13743240610&shp=81f88b70&shcp=55b124be6a9&idc=no1a",
      "playUrl": "https://v16-webapp-prime.tiktok.com/video/tos/alisg/tos-alisg-ve-37c71299-sg/oYjIxsdfXiCJC8yV9pxCsN8hGwIBsdffA8iBQAwAF1sE/?a=1988&bti=ODszNWYuMDE6&&bt=710&ft=-Csk_mgdPD12N1241HEEn-UxM4FSY3Wdsf3wv25-cAp&mime_type=video_mp4&rc=aTdfsdw1ZTllOTk0aDU2ZGg3NkBpajM6ZWs5cnhyZDMdsfsdfzZzczNEA2NDMsdgsdgsdgS5yMmRjYXJhLsdfS1kMS9zcw%3D%3D&expire=1792172212&l=20261014173125135253C84560A7483456&ply_type=2&policy=2&signature=7bddsg2g43t43wegfsf768999e0c21&tk=tt_chain_token&btag=e006230b8000",
      "downloadUrl": ""
    },
    "music": {
      "id": "12431241241",
      "title": "original sound",
      "author": "tiktok",
      "duration": 23,
      "cover": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/sdf2f34tetdxsfsfsdf~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=sdf2f34tetdxsfsfsdf&x-expires=1251251&x-signature=sdf2f34tetdxsfsfsdf%sadsaaf31fe%3D&t=4d5bfsd0474&ps=1374120610&shp=a5d48dsfsdfsf078&shcp=81f88b70&idc=no1a",
      "playUrl": "https://v45.tiktokcdn-eu.com/sdf2f34tetdxsfsfsdf/sdf2f34tetdxsfsfsdf/video/tos/alisg/tos-alisg-ve-2370c799-sg/sdf2f34tetdxsfsfsdf/?a=1233&bti=sdfsdfsdg32f&&bt=125&ft=sdf2f34tetdxsfsfsdf&mime_type=audio_mpeg&rc=sdfsdfghsdg%3D%3D&vvpl=1&l=20261014173629124305A43C84560A7483456&btag=e0010bd000&sp_exp=hash_v0",
      "album": null
    },
    "stats": {
      "plays": 12300,
      "likes": 985700,
      "comments": 161800,
      "shares": 892400,
      "saves": 667912
    },
    "stickers": [
      "Sept. 23, 2026"
    ],
    "challenges": [
      {
        "id": "21123848",
        "title": "update",
        "videos": 1356513
      },
      {
        "id": "1928129",
        "title": "news",
        "videos": 912337
      },
      {
        "id": "162316",
        "title": "oklahoma",
        "videos": 3142164
      },
      {
        "id": "1211272",
        "title": "ok",
        "videos": 6522521871
      }
    ],
    "author": {
      "id": "1251241312",
      "username": "tiktok",
      "nickname": "tiktok",
      "secUid": "MasdS4wLjABAAAAsP-2iHKASG214GexDPFr7VCRqCUdgadgGasGEGHSDEF0hLS8n-f",
      "avatar": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/a2edad9121b487092214022dcad516234838d6f19~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=2f13349c20&x-expires=17921170000&x-signature=AaH8GmDXeF3M%2BvoTWwGT215FAS1rfSJW4nM8%3D&t=4d5b0214474&ps=13740610&shp=a5d41248078&shcp=81f82148b70&idc=no1a",
      "bio": "Well.. TikTok.",
      "verified": true,
      "followerCount": 143100000,
      "followingCount": 15,
      "heartCount": 61300000000,
      "videoCount": 117900
    }
  }
}
"""