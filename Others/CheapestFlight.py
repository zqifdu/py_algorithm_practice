"""
Given a list of flights (starting city, ending city, price), find the cheapest flight(s) from A to B.

flights = [
 ["London", "Paris", "150"],
 ["London", "Istanbul", "75"],
 ["Istanbul", "Paris", "25"],
]

London -> Paris: cheapest flight is London -> Istanbul -> Paris (100)

"""
import heapq


def cheapestFlight(flights, starting_city, ending_city):
    city_graph = make_graph(flights) # { "starting city": (price, "destination") }

    price_heap = [(price_tuple[0], [starting_city, price_tuple[1]]) for price_tuple in city_graph[starting_city]]
    # price_heap = city_graph[starting_city]
    # make a min-heap
    heapq.heapify(price_heap) # heapq.heapify(city_graph[starting_city])
    visited = set()
    print(price_heap)


    while price_heap:
        price, path_to_city = heapq.heappop(price_heap)
        next_city = path_to_city[-1]
        visited.add(next_city)
        if next_city == ending_city:
            return price, path_to_city
        for add_price, next_next_city in city_graph[next_city]:
            if next_next_city in visited:
                continue

            new_price = add_price + price
            next_next_price_city = (new_price, path_to_city + [next_next_city])
            heapq.heappush(price_heap, next_next_price_city)
            # print(price_heap)


    return (float('inf'), None)
    # time:O(n)
    # space:O(n^2)


def make_graph(flights):
    city_graph = {}
    for start, end, price in flights:
        city_graph[start] = city_graph.get(start, []) + [(int(price), end)]
        city_graph[end] = city_graph.get(end, [])
    return city_graph

flights = [
 ["London", "Paris", "150"],
 ["London", "Istanbul", "75"],
 ["Istanbul", "Paris", "25"]
]

print(make_graph(flights))
print(cheapestFlight(flights, "London", "Paris"))
