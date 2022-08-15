from flask import Flask, Response
import requests
import json

app = Flask(__name__)


@app.route("/")
def search_in_yahoo_finance(ticker: str):
    headers = {
        'User-agent': 'Mozilla/5.0',
        # "pepito": "juanito"
    }
    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={ticker}&lang=en-US&region=US&quotesCount=6" \
          f"&newsCount=2&listsCount=2&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId" \
          f"=multi_quote_single_token_query&newsQueryId=news_cie_vespa&enableCb=true&enableNavLinks=true" \
          f"&enableEnhancedTrivialQuery=true&enableResearchReports=true&enableCulturalAssets=true" \
          f"&researchReportsCount=2 "
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == "__main__":
    print(search_in_yahoo_finance("KO"))


@app.route("/get-price/<ticker>")
def get_price(ticker, company_info=None):
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}&lang=en-US&region=US&quotesCount=6&newsCount=2&listsCount=2&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_cie_vespa&enableCb=true&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableResearchReports=true&enableCulturalAssets=true&researchReportsCount=2"

    f"print(company_info)"

    price = company_info['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    company_name = company_info['quoteSummary']['result'][0]['price']['longName']
    exchange = company_info['quoteSummary']['result'][0]['price']['exchangeName']
    currency = company_info['quoteSummary']['result'][0]['price']['currency']

    result = {
        "price": price,
        "name": company_name,
        "exchange": exchange,
        "currency": currency
    }
    print(result)

    return Response(json.dumps(result))


if __name__ == '__yahoo__':
    app.run()
