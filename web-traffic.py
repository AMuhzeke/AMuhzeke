import requests

def check_web_traffic(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Web traffic for {url} is good.")
        else:
            print(f"Web traffic for {url} is not as expected. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to check web traffic: ")
    check_web_traffic(url)
