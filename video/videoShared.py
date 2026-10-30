from einzztools import call
import json

status, data = call("video/videoShared", url="https://vm.tiktok.com/ZGdEasgda/")
print(status)
print(json.dumps(data, indent=2)[:12600])

# Example Output: 
"""
200
{
  "success": true,
  "data": {
    "success": true,
    "videoId": "123123123123123",
    "username": "tiktok",
    "sharerId": "123123123",
    "sharerUsername": "tiktok_news",
    "device": "android",
    "sharedAt": "2019-06-21T23:36:11.000Z",
    "landingUrl": "https://www.tiktok.com/@tiktok/video/12312312321?_d=secCgYIASAH1fasKAESPgo845sf2AGAGFAfgb8qtgGubVMFASesC5DTWX0mqafsKleHs05qYiJSSrGk68cWEAa4Ryv4gf9WwxDPYZtAdlGgA%3D&_r=1&_svg=2&biz_cover_on=1&card_desc_fallback=1&checksum=a868c8adg93011c0670214f4f6a175845e2b14124fe36825ff887cc1434a602fa4ebd6100&item_author_type=1&link_reflow_popup_iteration_sharer=%7B%22click_empty_to_play%22%3A1%2C%22dynamic_cover%22%3A1%2C%22follow_to_play_duration%22%3A-1.0%2C%22profile_clickable%22%3A1%7D&og_size_on=1&panel_source_v1=share_panel&preview_pb=1&reflow_page_type=1&reflow_sign_scene=1&rgssign=2.1.XttOGEASFABg7aCphTxc71h215ro2A&sec_user_id=MS4wLjHADGGGEgdhZHMIPRJPViiftfwz2kDadHSDgDSHGEEWIU&share_app_id=112233&share_enter_from=homepage_hot&share_item_id=345123414134&share_link_id=12312315c-123123-325-25asf-480b3d51780f&share_region=DE&share_scene=2&share_source=app_panel_share&sharer_language=en&social_share_type=0&source=h5_m&sp_level=1&sp_root_d=OIHSLFHLGNGIHPFOMIHPAOJFSPOJPMOASPFHAOSHFLASFHSALFHIAFHOHSADFIOA%3D&sp_root_share_link_id=32rfaf-e28asf1b-asf1-asg-asf2ffaf&sp_root_u=ek3asf0jl3geasfdmllm&timestamp=171282776171&u_code=ek30jl3gedmllm&ug_btm=b201201&ugbiz_name=MAIN&user_id=123124135151&utm_campaign=client_share&utm_medium=android&utm_source=telegram&vid_fwc_v6=1",
    "params": {
      "_d": "secCajSJFPpj1pfisHApfoHOIehfisdnlAhgKuGSHIfNou3ho2irLABSFIUHOIg1w1ff",
      "_r": "1",
      "_svg": "2",
      "biz_cover_on": "1",
      "card_desc_fallback": "1",
      "checksum": "asfgsdgajSJFPpj1pfisHApfoHOIehfisdnlAhgKuGSHIfNou3ho2irLABSFIUHOIg1w1ff",
      "item_author_type": "2",
      "link_reflow_popup_iteration_sharer": "{\"click_empty_to_play\":1,\"dynamic_cover\":1,\"follow_to_play_duration\":-1.0,\"profile_clickable\":1}",
      "og_size_on": "1",
      "panel_source_v2": "share_panel",
      "preview_pb": "0",
      "reflow_page_type": "1",
      "reflow_sign_scene": "1",
      "rgssign": "2.1.XttOGEAB7aCphTxc71ho2A",
      "sec_user_id": "MSICajSJFPpj1pfisHApfoHOIehfisdnlAhgKuGSHIfNou3ho2irLABSFIUHOIg1w1ff-fRATx-asfasp4PIU",
      "share_app_id": "1233",
      "share_enter_from": "homepage_hot",
      "share_item_id": "12516236251",
      "share_link_id": "asdasafa1-easd28b-4safafsad6-sad12-asgeg2eg",
      "share_region": "DE",
      "share_scene": "2",
      "share_source": "app_panel_share",
      "sharer_language": "en",
      "social_share_type": "0",
      "source": "h5_m",
      "sp_level": "1",
      "sp_root_d": "secCajSJFPpj1pfisHApfoHOIehfisdnlAhgKuGSHIfNou3ho2irLABSFIUHOIg1w1ff=",
      "sp_root_share_link_id": "125-e2128b-4a123123d6-2151-481240b31245d51780f",
      "sp_root_u": "sadfasrw1f",
      "timestamp": "123114125",
      "u_code": "c1wdasqwrwr",
      "ug_btm": "b2f001",
      "ugbiz_name": "MAIN",
      "user_id": "12414151351",
      "utm_campaign": "client_share",
      "utm_medium": "android",
      "utm_source": "telegram",
      "vid_fwc_v6": "1"
    },
    "shareRegion": "DE",
    "originalUrl": "https://vm.tiktok.com/125rfsff1/"
  }
}
"""
