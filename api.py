import requests,time
while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    a = data["bpi"]["USD"]["rate"]
    print(a)
    time.sleep(30)