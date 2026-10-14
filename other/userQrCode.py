from tiktrack import call
import json

status, data = call("other/userQrcode", userId="2131123213123", schemaType="4")
print(status)
print(json.dumps(data, indent=2)[:600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "success": true,
    "qrcodeUrl": "https://p16-sign-sg.tiktokcdn.com/tikcode-sg/7696570374343491591~tplv-tiktokx-cropcenter:720:720.webp?dr=14579&x-expires=1792018800&x-signature=G47uAlY4hb0D0wN%2FNyu8jXALzF0%3D&idc=my&ps=13740610&shcp=9b759fb9&shp=45744a80&t=4d5b0474",
    "timestamp": "2026-10-14T17:03:54.432Z"
  }
}
"""