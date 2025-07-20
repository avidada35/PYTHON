import requests

def randomDataFromNet():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        return username

    else:
        raise Exception("Failed to fetch random user data")
    
def main():
    try:
        username = randomDataFromNet()
        print(username)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()



