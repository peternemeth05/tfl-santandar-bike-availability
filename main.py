import requests
import xml.etree.ElementTree as ET # ElementTree is a builtin py library

from time import time 

def get_station_availability(station_name: str) -> str:

    XML_URL = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"
    # XML is formatted like a family tree
    #   -every document has one 'root' element (single ancestor from which everything branches)
    #   - our root element is <stations> -> <station> -> <'station characterstics' eg nbBikes, nbDocks> &

    try:
        response = requests.get(XML_URL, timeout = 10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    

    root = ET.fromstring(response.content)

    for station in root.findall('station'):
        name = station.find('name').text

        if name == station_name:
            total_bikes = station.find('nbBikes').text
            empty_docks = station.find('nbEmptyDocks').text
            ebikes = station.find('nbEBikes').text
            standard_bikes = station.find('nbStandardBikes').text


    print(f"\ntotal bikes is {total_bikes}, with {empty_docks} empty docks\n")
    #print((response.content[0:100]))


if __name__ == "__main__":
    t1 = time()

    get_station_availability("River Street , Clerkenwell")

    print(f"time for first station data {time()-t1}\n")

    t2 = time()

    get_station_availability("Victoria & Albert Museum, South Kensington")

    print(f"time for last station data {time()-t2}\n")


    pass