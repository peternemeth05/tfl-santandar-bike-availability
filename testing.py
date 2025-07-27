from main import get_station_availability
from time import time


if __name__ == '__main__':

    t1 = time()

    get_station_availability("River Street , Clerkenwell")

    print(f"time for first station data {time()-t1}\n")
    
    t2 = time()

    get_station_availability("Ansell House, Stepney")

    print(f"time for mid station data {time()-t2}\n")


    t3 = time()

    get_station_availability("Victoria & Albert Museum, South Kensington")

    print(f"time for last station data {time()-t3}\n")

    # all roughty the same as about 0.05 - 0.1 seconds

