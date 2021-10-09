import requests,time
while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    print(data["bpi"]["USD"]["rate"])
    time.sleep(30)
