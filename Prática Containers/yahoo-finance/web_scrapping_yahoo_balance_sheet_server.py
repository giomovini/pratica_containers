import pandas as pd
import yfinance as yf
import flask
from flask import Flask, jsonify

server = Flask(__name__)

@server.route("/")
def yahoo_finance():
    data = yf.download("msft aapl goog", period="12mo")
    
    return data.to_json(orient='records')

yahoo_finance()

if __name__ == "__main__":
   server.run(host='0.0.0.0')