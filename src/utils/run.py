import random
import time
from .display import display_simulation

def simulation(flight):
    layout = tuple(tuple(row) for row in flight._aircraft.layout)

    round = 1
    passengers_by_aisle = flight.get_passengers_by_aisle()
    for aisle, passengers in passengers_by_aisle.items():
        random.shuffle(passengers)
    while any(not passenger.is_seated and passenger.seat for passenger in flight._passengers):  # Verify if all passengers with seats are seated
        for aisle, seats in flight._aircraft.get_closest_seats_for_each_aisle().items():
            min_column = layout[0].index(seats[0])
            max_column = layout[-2].index(seats[-1])
            columns = list(range(min_column, max_column + 1))
            columns.remove(aisle)
            order = []
            # We take first the extreme columns and then the middle ones 
            while columns:
                order.append(columns.pop(0))
                if columns:
                    order.append(columns.pop(-1))
            order = order + [aisle]
            flight.boarding(order, passengers_by_aisle[aisle])
        display_simulation(flight, round)
        round += 1
        time.sleep(0.5)
    print("Boarding completed!")