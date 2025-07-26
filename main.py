import requests

def get_station_availability(station_name: str) -> str:

    XML_URL = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"

    try:
        response = requests.get(XML_URL, timeout = 10)

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

    print(response.content.strip())


if __name__ == "__main__":

    get_station_availability("River Street , Clerkenwell")


    pass