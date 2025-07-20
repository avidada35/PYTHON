import requests

def CompanyStock():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        company_name = data["data"]["Name"]
        market_cap = data["data"]["MarketCap"]
        current_price = data["data"]["CurrentPrice"]

        return company_name, market_cap, current_price
    else:
        raise Exception("Failed to fetch data")
    

def main():
    try:
        company_name, market_cap, current_price = CompanyStock()
        print()
        print("-------------------------")
        print(f"Company Name: {company_name} \nMarket cap: {market_cap} \nCurrent price: {current_price}")
        print("-------------------------")
        print()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

