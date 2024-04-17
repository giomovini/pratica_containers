import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
server = Flask(__name__)

@server.route("/")
def cash_balance_get():
    url = 'https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA'
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    
    cash_balance = {}
    
    main_content = soup.find_all('div', class_='M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)')
    for div in main_content:
        sub_div = div.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
        for sub in sub_div:
            cash_balance[sub.get_text(separator="|").split("|")[0]] = sub.get_text(separator="|").split("|")[1]
            print(sub.get_text())
            
    return jsonify(cash_balance)

if __name__ == "__main__":
   server.run(host='0.0.0.0')
