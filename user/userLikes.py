from einzztools import call
import json

status, data = call("user/userLikes", username="tiktok", cursor="0")
print(status)
print(json.dumps(data, indent=2)[:15600])

# Example Output: 
"""
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "123123123",
        "desc": "",
        "createTime": 1690588729,
        "author": {
          "id": "123123123",
          "uniqueId": "tiktok",
          "nickname": "TikTok",
          "signature": "tiktok",
          "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
          "verified": true,
          "privateAccount": false,
          "secret": false,
          "ftc": false,
          "isADVirtual": false,
          "isEmbedBanned": false,
          "avatars": {
            "thumb": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-avt-0068-euttp/873da24d34a264864a61160a2fc2ad68e7b3~tplv-tiktokx-cropcenter:100:100.jpeg?dr=10399&refresh_token=6211b5c262e&x-expires=179221750000&x-signature=zsbFJCDkVaPpAkAQsy%2FJYvxkW8yg%3D&t=4d5b05474&ps=137402610&shp=a5d481078&shcp=81f828b70&idc=no1a",
            "medium": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-avt-0068-euttp/8753da24d34a64864a26160afc2ad68e7b3~tplv-tiktokx-cropcenter:720:720.jpeg?dr=10399&refresh_token=feb3d222d&x-expires=179261570000&x-signature=xsrFygMfjHR5H5uXc3DYDSSyxkUQ%3D&t=4d25b0474&ps=132740610&shp=a5d482078&shcp=681f88b70&idc=no1a",
            "larger": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-avt-0068-euttp/587da2454d34a648564a56160afc2ad68e7b3~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=8690c6aef3&x-expires=172922170000&x-signature=lPxbwt1Lgi18QyLfOFZTXSbUHvrs%3D&t=4d5b04274&ps=1374660610&shp=a5d487078&shcp=817f88b70&idc=no1a"
          },
          "settings": {
            "comment": 0,
            "duet": 0,
            "download": 0,
            "stitch": 0,
            "openFavorite": false
          },
          "statsV2": {
            "diggCount": "124124049",
            "followerCount": "123123129600",
            "followingCount": "123",
            "friendCount": "20",
            "heart": "1232300000",
            "heartCount": "1232300000",
            "videoCount": "5259"
          }
        },
        "hashtagNames": [],
        "isCommerce": "",
        "duetEnabled": true,
        "duetDisplay": 0,
        "status": {
          "isAd": false,
          "isProhibited": false,
          "isReviewing": false,
          "itemCommentStatus": 0,
          "can_repost": true,
          "officalItem": false,
          "originalItem": false,
          "reviewed": 0
        },
        "video": {
          "PlayAddrStruct": {
            "DataSize": 11257123167,
            "FileCs": "c:0-9212399-7113bb",
            "FileHash": "2b04123b97bf3309f5825b5ebadde451d81",
            "Height": 1024,
            "Uri": "v26044gc0132000datrrpnog65ra3en4f1g",
            "UrlKey": "v1ctfc0000faf132zt32pnog65rsdg2eg4f1g_as64_540p_99g210",
            "UrlList": [
              "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
              "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
              "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
            ],
            "Width": 576
          },
          "VQScore": "66.75",
          "bitrate": 993112310,
          "bitrateInfo": [
            {
              "Bitrate": 1111236944,
              "BitrateFPS": 30,
              "CodecType": "h265_hvc1",
              "Format": "mp4",
              "GearName": "adapt_lowest_1080_1",
              "MVMAF": "{\"v2.0\": {\"srv1\": {\"v1080\": 96.174, \"v960\": 96.941, \"v864\": 97.484, \"v720\": 98.336}, \"ori\": {\"v1080\": 90.04, \"v960\": 91.324, \"v864\": 92.565, \"v720\": 94.211}}}",
              "PlayAddr": {
                "DataSize": 129021211,
                "FileCs": "c:0-9452-8f87",
                "FileHash": "2e4123b8a0f41231282236316f1241214289b7d1934767e70",
                "Height": 1920,
                "Uri": "v260412444gc0000da1212trrpnog65ra3e124n4f1g",
                "UrlKey": "afsf2f2feftsfgen4f1g_b12412580p_asfaaf3225235",
                "UrlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
                ],
                "Width": 1080
              },
              "QualityType": 2,
              "VideoExtra": "{\"PktOffsetMap\":\"[{\\\"time\\\": 1, \\\"offset\\\": 200154}, {\\\"time\\\": 2, \\\"offset\\\": 301197}, {\\\"time\\\": 3, \\\"offset\\\": 438003}, {\\\"time\\\": 4, \\\"offset\\\": 586675}, {\\\"time\\\": 5, \\\"offset\\\": 758409}]\",\"mvmaf\":\"{\\\"v2.0\\\": {\\\"srv1\\\": {\\\"v1080\\\": 96.174, \\\"v960\\\": 96.941, \\\"v864\\\": 97.484, \\\"v720\\\": 98.336}, \\\"ori\\\": {\\\"v1080\\\": 90.04, \\\"v960\\\": 91.324, \\\"v864\\\": 92.565, \\\"v720\\\": 94.211}}}\",\"ufq\":\"{\\\"enh\\\":81.754,\\\"playback\\\":{\\\"ori\\\":75.794,\\\"srv1\\\":81.928},\\\"src\\\":81.754,\\\"trans\\\":75.794,\\\"version\\\":\\\"v1.2\\\"}\",\"volume_info_json\":\"\",\"transcode_feature_id\":\"e91245375450b02a8794eaf362ea32ee\",\"dec_info\":\"\",\"gearvqm\":\"{\\\"v3.0\\\": {\\\"ori\\\": 98.24, \\\"sr20\\\": 108.059}}\",\"audio_bit_rate\":65297,\"ps_info\":\"{\\\"vps\\\": \\\"AQwC//8BYAAAAwAAAwAAAwAAAwCWAACIJElgSA==\\\", \\\"sps\\\": \\\"AQMBYAAAAwAAAwAAAwAAAwCWAACgAhyAHgWWIJElySUQTPCEREREREYR8xPOX+/+v82fy/+v8yh+S/3/1/mz+X/1/jOEAg5qAgICCAAAAwAIAAADAPBA\\\", \\\"pps\\\": \\\"AcElPAiQ\\\"}\"}"
            },
            {
              "Bitrate": 993110,
              "BitrateFPS": 30,
              "CodecType": "h264",
              "Format": "mp4",
              "GearName": "normal_540_0",
              "MVMAF": "{\"v2.0\": {\"srv1\": {\"v1080\": 90.466, \"v960\": 93.214, \"v864\": 94.558, \"v720\": 96.397}, \"ori\": {\"v1080\": 80.503, \"v960\": 83.166, \"v864\": 85.906, \"v720\": 89.25}}}",
              "PlayAddr": {
                "DataSize": 114127167,
                "FileCs": "c:0-9299-71bb",
                "FileHash": "2b09123b97bf331232509f581263c25b5ebad1e451232d84",
                "Height": 1024,
                "Uri": "v21236044gc0000datr123rpno123g65ra3en4f1123g",
                "UrlKey": "v26044gcasd0000da123trrpnog6asd5ra1233en4f1g_h264asd_540p_992133110",
                "UrlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
                ],
                "Width": 576
              },
              "QualityType": 20,
              "VideoExtra": "{\"PktOffsetMap\":\"[{\\\"time\\\": 1, \\\"offset\\\": 163532}, {\\\"time\\\": 2, \\\"offset\\\": 268920}, {\\\"time\\\": 3, \\\"offset\\\": 390380}, {\\\"time\\\": 4, \\\"offset\\\": 514750}, {\\\"time\\\": 5, \\\"offset\\\": 659831}]\",\"mvmaf\":\"{\\\"v2.0\\\": {\\\"srv1\\\": {\\\"v1080\\\": 90.466, \\\"v960\\\": 93.214, \\\"v864\\\": 94.558, \\\"v720\\\": 96.397}, \\\"ori\\\": {\\\"v1080\\\": 80.503, \\\"v960\\\": 83.166, \\\"v864\\\": 85.906, \\\"v720\\\": 89.25}}}\",\"ufq\":\"\",\"volume_info_json\":\"\",\"transcode_feature_id\":\"25b3faebdda74a9e438e851988a6efcc\",\"dec_info\":\"\",\"gearvqm\":\"\",\"audio_bit_rate\":32825}"
            },
            {
              "Bitrate": 645001,
              "BitrateFPS": 30,
              "CodecType": "h265_hvc1",
              "Format": "mp4",
              "GearName": "adapt_lower_720_1",
              "MVMAF": "{\"v2.0\": {\"srv1\": {\"v1080\": 91.791, \"v960\": 93.658, \"v864\": 94.883, \"v720\": 96.615}, \"ori\": {\"v1080\": 82.908, \"v960\": 85.129, \"v864\": 86.926, \"v720\": 90.392}}}",
              "PlayAddr": {
                "DataSize": 745057,
                "FileCs": "c:0-9452-1173",
                "FileHash": "3a552235249a389a0eab533e5aebb94562341246f894b8",
                "Height": 1280,
                "Uri": "v26567044gc5670000567datrr576pnog65ra3en4f1g",
                "UrlKey": "v26057644gc0000d675atrrpnog65ra3en4f1g_byt576evc1987_720p_687045001",
                "UrlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068-euttp/o4a5wLgNTIUEP7Emr0KiZg1uBvDyGXi7BA4A9/?a=1988&bti=ODszNWYuMDE6&&bt=629&ft=I~da4o3.D12Nv17eezIxRMkSYl-H-UjNSVopiX&mime_type=video_mp4&rc=PGRlPDVpPDxnZDNnZjYzZUBpamlxNnU5cnN1ZDMzZjczNUAvNjY0NTY1NjQxNWEvMDJeYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=5316b0ca2ae2c4456621a73dc68fcbbd&tk=tt_chain_token&btag=e000b0000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068-euttp/o4a5wLgNTIUEP7Emr0KiZg1uBvDyGXi7BA4A9/?a=1988&bti=ODszNWYuMDE6&&bt=629&ft=I~da4o3.D12Nv17eezIxRMkSYl-H-UjNSVopiX&mime_type=video_mp4&rc=PGRlPDVpPDxnZDNnZjYzZUBpamlxNnU5cnN1ZDMzZjczNUAvNjY0NTY1NjQxNWEvMDJeYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=5316b0ca2ae2c4456621a73dc68fcbbd&tk=tt_chain_token&btag=e000b0000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=ab50332cdd804a7d99899f82799b9a29&is_play_url=1&item_id=7690949576995474721&line=0&ply_type=2&pt=YXdlbWUud2ViLndlYmFwaSYvYXBpL2Zhdm9yaXRlL2l0ZW1fbGlzdC8mMjAyNjEwMTQxNzIxNDdDNEU2NThFOEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzNmRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZDtpdGVtX2lkLjYyNjNmNjQzYjg0ZDEzYTQ3ODFlOTQyYTcyNGFkNzE3&tk=tt_chain_token&video_id=v26044gc0000datrrpnog65ra3en4f1g"
                ],
                "Width": 720
              },
              "QualityType": 14,
              "VideoExtra": "{\"PktOffsetMap\":\"[{\\\"time\\\": 1, \\\"offset\\\": 116718}, {\\\"time\\\": 2, \\\"offset\\\": 167123}, {\\\"time\\\": 3, \\\"offset\\\": 242170}, {\\\"time\\\": 4, \\\"offset\\\": 328266}, {\\\"time\\\": 5, \\\"offset\\\": 426199}]\",\"mvmaf\":\"{\\\"v2.0\\\": {\\\"srv1\\\": {\\\"v1080\\\": 91.791, \\\"v960\\\": 93.658, \\\"v864\\\": 94.883, \\\"v720\\\": 96.615}, \\\"ori\\\": {\\\"v1080\\\": 82.908, \\\"v960\\\": 85.129, \\\"v864\\\": 86.926, \\\"v720\\\": 90.392}}}\",\"ufq\":\"{\\\"enh\\\":81.754,\\\"playback\\\":{\\\"ori\\\":69.185,\\\"srv1\\\":78.068},\\\"src\\\":81.754,\\\"trans\\\":69.185,\\\"version\\\":\\\"v1.2\\\"}\",\"volume_info_json\":\"\",\"transcode_feature_id\":\"cebe96cc7e15fab783061bbf7caef166\",\"dec_info\":\"\",\"gearvqm\":\"{\\\"v3.0\\\": {\\\"ori\\\": 93.083, \\\"sr20\\\": 100.183}}\",\"audio_bit_rate\":65297,\"ps_info\":\"{\\\"vps\\\": \\\"AQwC//8BYAAAAwAAAwAAAwAAAwC6AACIJElgSA==\\\", \\\"sps\\\": \\\"AQMBYAAAAwAAAwAAAwAAAwC6AACgBaIAUBZYgkSXJIkQTPCEREREREYR8xPOX+/+v82fy/+v8yh+S/3/1/mz+X/1/jOEAg5qAgICCAAAAwAIAAADAPBA\\\", \\\"pps\\\": \\\"AcElPAiQ\\\"}\"}"
            },
            {
              "Bitrate": 544449,
              "BitrateFPS": 30,
              "CodecType": "h264",
              "Format": "mp4",
              "GearName": "lower_540_0",
              "MVMAF": "{\"v2.0\": {\"srv1\": {\"v1080\": 79.743, \"v960\": 79.988, \"v864\": 83.455, \"v720\": 86.105}, \"ori\": {\"v1080\": 71.149, \"v960\": 73.606, \"v864\": 74.846, \"v720\": 78.783}}}",
              "PlayAddr": {
                "DataSize": 628235907,
                "FileCs": "c:0-9299-ce7e",
                "FileHash": "2c091235b1ef5d67321defeda1623599034663",
                "Height": 1024,
                "Uri": "v26044g235c0000datrrpnog65235ra3en4f1g",
                "UrlKey": "v2156044gc0000datrrpnog6512ra3en4f1g523125_h264_540p_544325449",
                "UrlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
                ],
                "Width": 576
              },
              "QualityType": 24,
              "VideoExtra": "{\"PktOffsetMap\":\"[{\\\"time\\\": 1, \\\"offset\\\": 87517}, {\\\"time\\\": 2, \\\"offset\\\": 140519}, {\\\"time\\\": 3, \\\"offset\\\": 204372}, {\\\"time\\\": 4, \\\"offset\\\": 271216}, {\\\"time\\\": 5, \\\"offset\\\": 350287}]\",\"mvmaf\":\"{\\\"v2.0\\\": {\\\"srv1\\\": {\\\"v1080\\\": 79.743, \\\"v960\\\": 79.988, \\\"v864\\\": 83.455, \\\"v720\\\": 86.105}, \\\"ori\\\": {\\\"v1080\\\": 71.149, \\\"v960\\\": 73.606, \\\"v864\\\": 74.846, \\\"v720\\\": 78.783}}}\",\"ufq\":\"\",\"volume_info_json\":\"\",\"transcode_feature_id\":\"25b3faebdda74a9e438e851988a6efcc\",\"dec_info\":\"\",\"gearvqm\":\"\",\"audio_bit_rate\":32825}"
            },
            {
              "Bitrate": 48265087,
              "BitrateFPS": 30,
              "CodecType": "h265_hvc1",
              "Format": "mp4",
              "GearName": "adapt_540_1",
              "MVMAF": "{\"v2.0\": {\"srv1\": {\"v1080\": 90.1, \"v960\": 91.665, \"v864\": 94.04, \"v720\": 95.398}, \"ori\": {\"v1080\": 77.795, \"v960\": 80.992, \"v864\": 83.13, \"v720\": 87.029}}}",
              "PlayAddr": {
                "DataSize": 43453521556871,
                "FileCs": "c:0-9452-8ffe",
                "FileHash": "2123346363634634643533a9e1dfe",
                "Height": 1024,
                "Uri": "v26012346346346250datrrpnog65ra3en4f1g23",
                "UrlKey": "v2604as124d4g21246c0000datr12421412526464363540p61162087",
                "UrlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
                ],
                "Width": 551276
              },
              "QualityType": 218,
              "VideoExtra": "{\"PktOffsetMap\":\"[{\\\"time\\\": 1, \\\"offset\\\": 88714}, {\\\"time\\\": 2, \\\"offset\\\": 124911}, {\\\"time\\\": 3, \\\"offset\\\": 178736}, {\\\"time\\\": 4, \\\"offset\\\": 239833}, {\\\"time\\\": 5, \\\"offset\\\": 311626}]\",\"mvmaf\":\"{\\\"v2.0\\\": {\\\"srv1\\\": {\\\"v1080\\\": 90.1, \\\"v960\\\": 91.665, \\\"v864\\\": 94.04, \\\"v720\\\": 95.398}, \\\"ori\\\": {\\\"v1080\\\": 77.795, \\\"v960\\\": 80.992, \\\"v864\\\": 83.13, \\\"v720\\\": 87.029}}}\",\"ufq\":\"{\\\"enh\\\":81.754,\\\"playback\\\":{\\\"ori\\\":65.35,\\\"srv1\\\":77.655},\\\"src\\\":81.754,\\\"trans\\\":65.35,\\\"version\\\":\\\"v1.2\\\"}\",\"volume_info_json\":\"\",\"transcode_feature_id\":\"0fb9126be2a766a8dd0f51cc544b234d\",\"dec_info\":\"\",\"gearvqm\":\"{\\\"v3.0\\\": {\\\"ori\\\": 88.987, \\\"sr20\\\": 98.042}}\",\"audio_bit_rate\":32825,\"ps_info\":\"{\\\"vps\\\": \\\"AQwC//8BYAAsdfAAwAAAwAAAwAAAwC6AACIJElgSA==\\\", \\\"sps\\\": \\\"AQMBYAAAAwAAAwAdfsaAAwAAAwC6AACgBIIAQBZYgkSXJIkQTPCEREREREYR8xPOX+/+v82fy/+v8yh+S/3/1/mz+X/1/jOEAg5qAgICCAAAAwAIAAADAPBA\\\", \\\"pps\\\": \\\"AcElPAiQ\\\"}\"}"
            }
          ],
          "claInfo": {
            "captionInfos": [
              {
                "captionFormat": "webvtt",
                "claSubtitleID": "123125632",
                "expire": "124125352345",
                "isAutoGen": true,
                "isOriginalCaption": true,
                "language": "fra-FR",
                "languageCode": "fr",
                "languageID": "7",
                "subID": "-125465563435",
                "subtitleType": "1",
                "translationType": "0",
                "url": "https://v16-webapp.tiktokcdn-eu.com/9cd17cf1c7fa5544a122e711ea321124b9fbb/6ad21245d35/video/tos/useast2a/tos-useast2a-v-0037-euttp/c1fcda1c18f5412462596e58d9e7c96042f/?a=1988&bti=ODszNWY124uMDE1236&&bt=3394&ft=4d51234~OPI~2NvjVNh__TzfuqglcAnBnR132Qjl9PXtG&mime_type=video_mp4&rc=amlxNnU5cnN1ZDMz1321ZjczNUBpamlxNnU56cnN1ZDMzZ4jczNUAuMWJeMm124Rrb3FhLSß1kMTNzYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&l=2026101454364172147C4E658E8AF5A75445BED&btag=e0007124000",
                "urlList": [
                  "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-00618c1001-euttp/oMEGXvV3Aej8dsINQIL3ALzgRGfagmMdYIDMUsdfseLft/?a=1988&bti=ODafszNW124YuMasfDE6&&bt=969&ft=I~da4o3.Dasf12Nv17easf24ezIx12asfRasfMkSYl42-H-asfUjNSafsVop44asfiX&mime_type=video_mp4&rc=PD4k7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNT567VfYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=202622210141172147C4E61258E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc123125845011a9e5125172ea98034&tk=tt_chain_token&btag=e00213102131230000",
                  "https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-001468c30051-euttp/oMEGXvV3Aej8INQdsf1IL3ALzgRGu12ggmMdaYIDdfMUeLft/?a=1988&bti=ODsasdzNdfWYuMDE6&&bt=969&ft=I~da4o3.afDasf12Nv1sdf47eezIxRMkSYl-H-Uj4NSasfV4opiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNm4dlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3765FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C4E658E8AF5A75445BED&ply_type=2&policy=2&signature=6sf739fc7d512912445011a12412172ea98034&tk=tt_chain_token&btag=e00123000",
                  "https://www.tiktok.com/aweme/v1/play/?faid=1988&file_id=b08c8d164eb5d44381c934ac19be21f138c614d9&is_play_url=a1&item_id=76129094124957642199547124721&line=0&ply_type=1&pt=YXdlbdsfWUud2VisdLndlYmFwaSYvYXBpL2Zsd4fhdm9yaXRlL24afsl0ZW1fbGlzdC8mMjAyNjEwMTQx4NzIxNDdDNEU2N4ThF4OEFGNUE3NTQ0NUJFRCYxNzkxOTk4NTA4JmEzN24mRiNmIyZDZhMw&signaturev3=dmlkZW9faWQ7ZmlsZV9pZ568DtpdGVtX2lkLjYxYjU3ZT8YxNGIyZDdjZThlNjQyMTY2MzFhODE4MGFi&tk=tt_chain_token&video_id=1v21260a44gcasd0612000da21sfrpnog65ra35eaasn4f1g"
                ],
                "variant": "whisper_lid"
              }
            ],
            "captionsType": 1,
            "enableAutoCaption": true,
            "hasOriginalAudio": false,
            "originalLanguageInfo": {
              "canTranslateRealTimeNoCheck": true,
              "language": "fra-FR",
              "languageCode": "fr",
              "languageID": "7"
            }
          },
          "codecType": "h264",
          "cover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/o8RXsfsfe31QGgLe125MssfsdgutasfasfavAILFMxjN8Dessdg8VXGQICg3Id~tp125lv-tiktokx-origin.image?dr=10395&x-expires=17921730000&x-signature=8MgMJ2fsk7R3bKNsWvW7X6x2k0Q%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
          "definition": "540p",
          "downloadAddr": "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068-euttp/owussgdgsgdgsgsgdgsd24124RMeDjQNfet8124q93IXAIGMKg/?a=1988&bti=ODszNWYuMDE6&&bt=1009&ft=I~da4o3.D12Nv17eezIxRMkSYl-H-UjNSVopiX&mime_type=video_mp4&rc=Njc5Z2Q2ZDQ2NTozZDZoOEBpamlxNnU5cnN1ZDMzZjczNUBhMzVhNC9eNjQxMzYzNC1hYSMuMW124JeMmRrb3FhLS1kMTNzcw%3D%3D&expire=1792171317&l=20261014172147C124124E658E8AF5A75445BED&ply_type=2&policy=2&signature=05f31d1e3cecd1292cc31437b0787865&tk=tt_chain_token&btag=e000b0000",
          "duration": 9,
          "dynamicCover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/sdffsdQ9IMe3uIsdfsdfsdfsdfdLgl03V8vQqL~tplv-tiktokx-origin.image?dr=10395&x-expires=1792170000&x-signature=fG73vo2xyLTZr3aQ9oMbfGs8%2FFQ%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
          "encodeUserTag": "",
          "encodedType": "normal",
          "format": "mp4",
          "height": 1024,
          "id": "7690949576995474721",
          "originCover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/okiIILLd8gGaNsdfsdgsgdgshsdh3e3eD~tplv-tiktokx-origin.image?dr=10395&x-expires=1792170000&x-signature=h594mEnQeE6mcBNwpYV3yDYfhsM%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a",
          "playAddr": "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c001-euttp/oMEGXvV3AeshdMUeLft/?ah=1988&bti=ODszNWYuMDE6&&bt=969&ft=I~da4o3.D12Nv17eezIxRMkSYl-H-UjNSVopiX&mime_type=video_mp4&rc=PDk7aTVlZjZmNmdlN2dmM0BpamlxNnU5cnN1ZDMzZjczNUBhYDAuYjZeNjUxMmIzNTVfYSMuMWJeMmRrb3FhLS1kMTNzcwsaf%3D%3D&expire=1792171317&l=20261014172147C4E651241248E8AF5A75445BED&ply_type=2&policy=2&signature=6739fc7d5129845011a9e1172ea98034&tk=tt_chain_token&btag=e00070000",
          "ratio": "540p",
          "size": 1147167,
          "subtitleInfos": [
            {
              "Format": "webvtt",
              "LanguageCodeName": "fra-FR",
              "LanguageID": "7",
              "Size": 264,
              "Source": "ASR",
              "Url": "https://v16-webapp.tiktokcdn-eu.com/9cd17c124124f1c7fa5544a2sdf124e711ea321b9fbb/6ad25d35/video/tos/useast2a/tos-useast2a-v-0037-euttp/c1fcda1c18f5462596e58d9e7c96042f/?a=1988&bti=ODszNWYuMDE6&&bt=3394&ft=4d54~OPI~2NvjVNh__TzfuqglcAsafasfnBnRQjl9PXtG&mime_type=video_mp4&rc=amlxNnU5cnN1ZDMzZjczNUBpamlxNnU5cnN1ZDMzZjasfczNUAuMWJeMmRrb3FhLS1kMTNzYSMuMWJeMmRrb3FhLS1kMTNzcw%3D%3D&l=20261014172147C4E658E8AF5A75445BED&btag=e00070000",
              "UrlExpire": 1792171317,
              "Version": "1:whisper_lid"
            }
          ],
          "videoID": "v26044gc0000datrrpnog65ra3en4f1g",
          "videoQuality": "normal",
          "volumeInfo": {
            "Loudness": -16,
            "Peak": 0.33113
          },
          "width": 576,
          "zoomCover": {
            "240": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/o8RXedf31QfddffdfGgLeMutvAILFMxjN8Dedfd8VXGQICg3Id~tplv-photomode-zoomcover:240:240.avif?dr=10375&x-expires=1792170000&x-signature=VaWHymc5rD67PpwwJasfdsfsdRXbkBYvMIw%3D&t=4d5b0474&ps=13740610&shp=8234f88b70&shcp=43f4324a2f9&idc=no1a&ftpl=1",
            "480": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/o8RXe31QddfdfGdfdfgLeMutvdfAILFMxjNdf8De8VXGQICg3Id~tplv-photomode-zoomcover:480:480.avif?dr=10375&x-expires=1792170000&x-signature=HRGuQqXyrKdsfsXYidVtZcflomrPAU%3D&t=4d5b0474&ps=13740610&shp=84321f88b70&shcp=43f4a2f3r249&idc=no1a&ftpl=1",
            "720": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-eudfttp/o8RXe31dfdfQGgLeMutdfvAILFMxjN8Dfdfe8VXGQdfdfICg3Id~tplv-photomode-zoomcover:720:720.avif?dr=10375&x-expires=1792170000&x-signature=aL4Ga1tsdfsdfX2QNa%2BaoRC5BsxFhWLtQ%3D&t=4d5b0474&ps=131233740610&shp=81f88b70&shcp=43ffsdf4a2f9&idc=no1a&ftpl=1",
            "960": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/o8RXe31dfdfQGgLeMutddffvAILFMxdfjN8Dedf8VXGQICg3Id~tplv-photomode-zoomcover:960:960.avif?dr=10375&x-expires=1792170000&x-signature=oK74W2LROP1VUF7AaOu4ML5ag%sdfsdf2BI%3D&t=4d5b0474&ps=13123740610&shp=81f88b70&shcp=43f4a2234f9&idc=no1a&ftpl=1"
          }
        },
        "music": {
          "authorName": "PR1NSE",
          "coverLarge": "https://p16-common-sign.tiktokcdn-eu.com/tos-alisg-avt-0068/a948ad01f3sdfsfsdfsdf6cf9b02b~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=10399&refresh_token=20d62r535ee&x-expires=179217200020&x-signature=nQa3IG7i6GABAFgNPjwLHWpWfTb2fsaf0%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88bGASS70&idc=no1a",
          "coverMedium": "https://p19-common-sign.tiktokcdn-eu.com/tos-alisg-avt-0068/a948ad01sdfsdfsfdsf446cf9b02b~tplv-tiktokx-cropcenter:720:720.jpeg?dr=10399&refresh_token=cb3af9628r75&x-expires=1729217002002&x-signature=%2BS7nGADw9l04EOwPN0asfUC74zB3ql9mA%3D&t=4d5FAb0474&ps=13740610&shp=a5dG2348078&shcp=81f88b70&idc=no1a",
          "coverThumb": "https://p16-common-sign.tiktokcdn-eu.com/tos-alisg-avt-0068/a948ad01f3sdfdsfsdfsf46cf9b02b~tplv-tiktokx-cropcenter:100:100.jpeg?dr=10399&refresh_token=32be1fe6bg&x-expires=179222170000&x-signature=LzbbJGVdyEFAGAwryik%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88GEb70&idc=no1a",
          "duration": 15,
          "id": "12516525345234234234",
          "isCopyrighted": true,
          "is_commerce_music": true,
          "is_unlimited_music": false,
          "original": true,
          "playUrl": "https://v45.tiktokcdn-eu.com/afsFGAGSG13faFW/afsFGAGSG13faFW/video/tos/alisg/tos-alisg-v-27dcd7/afsFGAGSG13faFW/?a=12512&bti=ODszNWYuMDE6&&bt=125&ft=cD1VS7z7ThWHTrSSLGZmo0P&mime_type=audio_mpeg&rc=ZGhoOTdpOzg5ZThoNWlkNUBpajNtOnk5cjttZDMzODU8NEBiMi4xMDYxNmAxYjU0Mi00YSNqbzFvMmQ0ZmBhLS1kMS1zcw%3D%3D&vvpl=1&l=20261014172147C4E658E8AF5A75445BED&btag=e000bd000&sp_exp=hash_v0",
          "private": false,
          "shoot_duration": 15,
          "title": "Zasf1"
        },
        "stickersOnItem": [],
        "effectStickers": [
          {
            "ID": "125125125",
            "name": "Darkness Aesthetic",
            "stickerStats": {
              "useCount": 0
            }
          },
          {
            "ID": "3252356546",
            "name": "chilly",
            "stickerStats": {
              "useCount": 0
            }
          },
          {
            "ID": "98785463",
            "name": "simple freckles",
            "stickerStats": {
              "useCount": 0
            }
          }
        ]
      }
    ],
    "totalReturned": 515,
    "nextCursor": "17789544720"
  }
}
"""
