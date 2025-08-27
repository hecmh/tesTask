import requests

def parse(response: dict) -> list[str]:

    logins: list[str] = []

    def extract_users(data):
        if isinstance(data, dict):
            if "login" in data and "id" in data:
                if not str(data["id"]).startswith("robot"):
                    logins.append(data["login"])
            for value in data.values():
                extract_users(value)
        elif isinstance(data, list):
            for item in data:
                extract_users(item)

    extract_users(response)
    return logins


if __name__ == "__main__":
    
    url = "https://search.yandex-team.ru/suggest/?text=Саптех&version=2&people.per_page=10"


    response = requests.get(url)
    response_dict = response.json()

    logins = parse(response_dict)
    print(logins)