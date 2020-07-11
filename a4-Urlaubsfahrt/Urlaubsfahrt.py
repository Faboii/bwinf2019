
def get_information_for_processing():
    file_data = get_data_from_file()
    CONSUMPTION_PER_KM, TANK_SIZE, INITIAL_FILLING, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS, \
    OIL_STATIONS_PRICE_PER_LITER = convert_file_data_to_usable_data(file_data)

    MAX_REACH = TANK_SIZE / CONSUMPTION_PER_KM
    START_REACH = INITIAL_FILLING / CONSUMPTION_PER_KM

    return START_REACH, MAX_REACH, CONSUMPTION_PER_KM, TANK_SIZE, INITIAL_FILLING, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS, OIL_STATIONS_PRICE_PER_LITER


def convert_file_data_to_usable_data(file_data):
    file_data = remove_spaces_and_empty_elements_from_list(file_data)
    CONSUMPTION_PER_KM_PER_100_KM = float(file_data[0])
    CONSUMPTION_PER_KM = CONSUMPTION_PER_KM_PER_100_KM / 100
    TANK_SIZE = float(file_data[1])
    INITIAL_FILLING = float(file_data[2])
    TOTAL_DISTANCE = float(file_data[3])

    DISTANCES_FROM_START_OF_OIL_STATIONS = []
    OIL_STATIONS_PRICE_PER_LITER = []
    for element in file_data[5:]:
        splitted_element = element.split(" ")
        splitted_element = remove_spaces_and_empty_elements_from_list(splitted_element)
        DISTANCES_FROM_START_OF_OIL_STATIONS.append(int(splitted_element[0]))
        OIL_STATIONS_PRICE_PER_LITER.append(int(splitted_element[1]))
    return CONSUMPTION_PER_KM, TANK_SIZE, INITIAL_FILLING, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS, OIL_STATIONS_PRICE_PER_LITER

def remove_spaces_and_empty_elements_from_list(untidy_list):
    tidied_data = []
    for element in untidy_list:
        element.strip()
        if not len(element) == 0:
            tidied_data.append(element)
    return tidied_data

def get_data_from_file():
    with open("/home/fabi/1_2/Development/SublimeProjects/Dev_Python/BWInf_2019/Urlaubsfahrt/beispieldaten/fahrt1.txt", "r") as file:
        file_as_string = file.read()

    file_as_list = file_as_string.split("\n")
    return file_as_list

def calc_smallest_amount_of_oil_stations_to_visit():
    global START_REACH, MAX_REACH, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS
    driven_distance = 0
    achievable_distance_from_start = driven_distance + START_REACH
    visited_oil_stations = 0

    while achievable_distance_from_start < TOTAL_DISTANCE:
        driven_distance = get_oil_station_with_most_achievable_distance_from_start(achievable_distance_from_start, DISTANCES_FROM_START_OF_OIL_STATIONS)
        achievable_distance_from_start = driven_distance + MAX_REACH
        visited_oil_stations += 1


    return  visited_oil_stations

def get_oil_station_with_most_achievable_distance_from_start(achievable_distance_from_start, DISTANCES_FROM_START_OF_OIL_STATIONS):

    # the oil stations are already sorted from lowest to greatest distance

    for oil_station_distance_from_start in DISTANCES_FROM_START_OF_OIL_STATIONS:

        if oil_station_in_reach(oil_station_distance_from_start, achievable_distance_from_start):
            distance_of_oil_station_with_greatest_distance_from_start = oil_station_distance_from_start

        # distance_of_oil_station_with_greatest distance_distance_from_start saves now the distance from start of the
        # oil station which has the greatest distance from start

    return distance_of_oil_station_with_greatest_distance_from_start

def oil_station_in_reach(oil_station_distance_from_start ,achievable_distance_from_start):
    achievable_distance_from_start
    if int(oil_station_distance_from_start) <=  achievable_distance_from_start:
        return True
    else:
        return False

def calc_every_possible_order_of_oil_stations_with_smallest_amount_of_stops(smallest_amount_of_stops):
    global START_REACH, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS

    for oil_station in DISTANCES_FROM_START_OF_OIL_STATIONS:
        if oil_station_in_reach(oil_station,START_REACH):
            possability_of_stops = [oil_station]
            get_next_stop(possability_of_stops, smallest_amount_of_stops)

def get_next_stop(possability_of_stops, smallest_amount_of_stops):
    global MAX_REACH, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS
    recent_distance = possability_of_stops[-1]
    possible_distance = recent_distance + MAX_REACH
    index_of_recent_oil_station = DISTANCES_FROM_START_OF_OIL_STATIONS.index(recent_distance)

    if possible_distance >= TOTAL_DISTANCE:
        global every_possible_order_of_oil_stations_with_smallest_amount_of_stops
        every_possible_order_of_oil_stations_with_smallest_amount_of_stops.append(possability_of_stops[:])

    elif len(possability_of_stops) < smallest_amount_of_stops:
        for oil_station in DISTANCES_FROM_START_OF_OIL_STATIONS[index_of_recent_oil_station:]:
            if oil_station_in_reach(oil_station,possible_distance):
                possability_of_stops.append(oil_station)
                get_next_stop(possability_of_stops, smallest_amount_of_stops)
                possability_of_stops.pop(-1)


def get_cheapest_route():
    global every_possible_order_of_oil_stations_with_smallest_amount_of_stops
    price_for_every_route = calc_price_for_every_route()
    print("price for every route",price_for_every_route)
    cheapest_route = find_cheapest_route(price_for_every_route) #TODO function not defined yet
    return cheapest_route

def find_cheapest_route(price_for_every_route):
    global every_possible_order_of_oil_stations_with_smallest_amount_of_stops

    cheapest_price = price_for_every_route[0]
    for price_for_route in price_for_every_route:
        if price_for_route < cheapest_price:
            cheapest_price = price_for_route

    index_of_cheapest_route = price_for_every_route.index(cheapest_price)
    return every_possible_order_of_oil_stations_with_smallest_amount_of_stops[index_of_cheapest_route]




def calc_price_for_every_route():
    global every_possible_order_of_oil_stations_with_smallest_amount_of_stops

    prices_for_every_route = []
    for route in every_possible_order_of_oil_stations_with_smallest_amount_of_stops:
        price_for_this_route = calc_price_for_this_route(route)
        prices_for_every_route.append(price_for_this_route)

    return prices_for_every_route

def calc_price_for_this_route(route):
    price = 0
    for oil_station in route:
        distance_to_tank_for = calc_distance_to_tank_for(route, oil_station)
        litres_to_tank = calc_litres_to_tank(distance_to_tank_for)
        price += calc_price_to_tank_for_at_this_oil_station(litres_to_tank, oil_station)

    return price

def calc_price_to_tank_for_at_this_oil_station(litres_to_tank, oil_station):
    global OIL_STATIONS_PRICE_PER_LITER, DISTANCES_FROM_START_OF_OIL_STATIONS

    price_per_litre = OIL_STATIONS_PRICE_PER_LITER[DISTANCES_FROM_START_OF_OIL_STATIONS.index(oil_station)]
    price_to_tank_for = litres_to_tank * price_per_litre
    return  price_to_tank_for


def calc_litres_to_tank(distance_to_tank_for):
    global CONSUMPTION_PER_KM

    litres_to_tank = distance_to_tank_for * CONSUMPTION_PER_KM

    return litres_to_tank




def calc_distance_to_tank_for(route, oil_station):
    global OIL_STATIONS_PRICE_PER_LITER, DISTANCES_FROM_START_OF_OIL_STATIONS

    price_per_liter_at_this_oil_station = OIL_STATIONS_PRICE_PER_LITER[DISTANCES_FROM_START_OF_OIL_STATIONS.index(oil_station)]
    possible_distance = oil_station + MAX_REACH

    if TOTAL_DISTANCE <= possible_distance:
        distance_to_tank_for = TOTAL_DISTANCE - oil_station
    else:
        price_per_liter_at_next_oil_station = OIL_STATIONS_PRICE_PER_LITER[DISTANCES_FROM_START_OF_OIL_STATIONS.index(route[route.index(oil_station) + 1])]
        if price_per_liter_at_this_oil_station < price_per_liter_at_next_oil_station:
            distance_to_tank_for = MAX_REACH
        else:
            distance_to_tank_for = route[route.index(oil_station) + 1] - oil_station

    return distance_to_tank_for




if __name__ == "__main__":
    # getting needed data for processing
    # this variables have to be available for other functions
    START_REACH, MAX_REACH, CONSUMPTION_PER_KM, TANK_SIZE, INITIAL_FILLING, TOTAL_DISTANCE, DISTANCES_FROM_START_OF_OIL_STATIONS, \
    OIL_STATIONS_PRICE_PER_LITER = get_information_for_processing()

    every_possible_order_of_oil_stations_with_smallest_amount_of_stops = []

    #processing
    smallest_amount_of_stops = calc_smallest_amount_of_oil_stations_to_visit()

    if smallest_amount_of_stops != 0:
        calc_every_possible_order_of_oil_stations_with_smallest_amount_of_stops(smallest_amount_of_stops)
        cheapest_route = get_cheapest_route()
        price_for_cheapest_route = calc_price_for_this_route(cheapest_route)
    else:
        print("finish in start range or no oil station in range")



    #output
    print("start reach:", START_REACH)
    print("max reach:", MAX_REACH)
    print("consumption per km:", CONSUMPTION_PER_KM)
    print("tank size", TANK_SIZE)
    print("initial filling", INITIAL_FILLING)
    print("total distance", TOTAL_DISTANCE)
    print("distances from start of oil stations", DISTANCES_FROM_START_OF_OIL_STATIONS)
    print("oil stations price per liter", OIL_STATIONS_PRICE_PER_LITER)
    print("smallest amount of stops", smallest_amount_of_stops)
    print("every possible order of oil stations with smallest amount of stops", every_possible_order_of_oil_stations_with_smallest_amount_of_stops)
    print("cheapest route",cheapest_route)
    print("price for cheapest route", price_for_cheapest_route)
    #print("cheapest route:",cheapest_route)
