import requests
print(requests.get(f'http://artii.herokuapp.com/make?text=iwcd').text)
print("[<3] Made With Love By insta : @iwcd , telagram @hhe1h")
email = input("Email : ")
password = input("Password : ")
url = "https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas="
head = {
    "User-Agent": "Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z",
    "Host": "api2.musical.ly",
    "Connection": "keep-alive",
}
data = {"email": email,"password": password}
rr = requests.post(url,headers=head,data=data)
if "user_id" in rr.text:
    ssesion  = print(rr.json()['data']['session_key'])
    input("Press Enter To Exit : ")
elif "Incorrect account or password" in rr.text:
    print('Incorrect account or password!')
    input("Press Enter To Exit : ")