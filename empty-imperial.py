import requests
import xml.etree.ElementTree as ET # ElementTree is a builtin py library


def get_station_availability(station_name: str) -> list:

    XML_URL = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"
    # XML is formatted like a family tree
    #   -every document has one 'root' element (single ancestor from which everything branches)
    #   - our root element is <stations> -> <station> -> <'station characterstics' eg nbBikes, nbDocks> &

    try:
        response = requests.get(XML_URL, timeout = 10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    
    bike_data = []

    root = ET.fromstring(response.content)

    for station in root.findall('station'):
        name = station.find('name').text

        if name == station_name:
            total_bikes = station.find('nbBikes').text
            bike_data.append(total_bikes)

            empty_docks = station.find('nbEmptyDocks').text
            bike_data.append(empty_docks)

            ebikes = station.find('nbEBikes').text
            bike_data.append(ebikes)

            standard_bikes = station.find('nbStandardBikes').text
            bike_data.append(standard_bikes)


    return bike_data #[total_bikes, empty_docks, ebikes, standard_bikes]





hux = get_station_availability("Imperial College, Knightsbridge")
rsm = get_station_availability("Prince Consort Road, Knightsbridge")
entrance = get_station_availability("Exhibition Road, Knightsbridge")
gloucester_road = get_station_availability("Gloucester Road (Central), South Kensington")
joe = get_station_availability("Gloucester Road (North), Kensington")


if hux[1] == rsm[1] == entrance[1] == 0: # if the number of empty docks equals 0
    print("There are no bike stations avaliable near Imperial Campus\n")

    if gloucester_road[1] != 0 and joe[1] != 0:
        print(f"\nThere are {gloucester_road[1]} empty docks on gloucester road, and {joe[1]} empty docks by Joe and The Juice\n")

if hux[1] != 0:
    print(f"\nHuxley bike station has {hux[1]} empty docks!\n")

if rsm[1] != 0:
    print(f"\nRSM bike station has {rsm[1]} empty docks!\n")

if entrance[1] != 0:
    print(f"\nMain entrance bike station has {entrance[1]} empty docks!\n")
        


