import copy
import os
import time
from emoji import emojize
import random
from .passenger import Passenger  # Importing the Passenger class (assumed to handle passenger details)
from .aircraft import Aircraft  # Importing the Aircraft class
from .seat import Seat  # Importing the Seat class

class Flight:
    """
    A class representing a flight, including its passengers, aircraft, and boarding process.
    """
    
    def __init__(self, aircraft: Aircraft):
        """
        Initializes a Flight object.

        Args:
            aircraft (Aircraft): The aircraft assigned to this flight.
        """
        self._aircraft = copy.deepcopy(aircraft)  # Deep copy of the aircraft to avoid modifying the original object
        self._seats = self._aircraft.seats  # Reference to the seats of the aircraft
        self._passengers = []  # List of passengers on the flight
        self.sell_seats()  # Sell seats to passengers upon initialization

    # Getter for the aircraft
    @property
    def aircraft(self):
        return self._aircraft

    # Getter for the seats
    @property
    def seats(self):
        return self._seats

    # Getter and setter for the passengers
    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, new_passengers):
        self._passengers = new_passengers

    def sell_seats(self):
        """
        Simulates selling seats to passengers. Randomly determines the number of seats sold,
        creates Passenger objects, and assigns them seats.
        """
        # Randomly determine the number of seats sold (95% to 100% capacity)
        seats_to_sell = random.randint(int(0.95 * self._aircraft.capacity), int(self._aircraft.capacity*1.03))
        
        # Create passengers (70% chance each passenger has baggage)
        self.passengers = [Passenger(self, random.random() <= 0.7) for _ in range(seats_to_sell)]

        # Copy and shuffle the list of available seats
        available_seats = self.seats.copy()
        random.shuffle(available_seats)

        # Assign seats to passengers
        for passenger in self.passengers:
            if available_seats:
                seat = available_seats.pop()
                passenger.seat = seat  # Assign a seat to the passenger
            else:
                print("Warning: No more seats available for remaining passengers.")
                break

    def boarding(self, order, passengers):
        """
        Simulates the boarding process of passengers onto the aircraft.

        Args:
            order (list): The boarding order of column indices.
            passengers (list): The list of passengers boarding.
        """
        layout = self._aircraft.layout  # Get the aircraft's seating layout

        def _passenger_aisle_case(layout, row, column):
            """
            Handles the movement of a passenger in an aisle.

            Args:
                layout (list): The aircraft's seating layout.
                row (int): The current row of the passenger.
                column (int): The current column of the passenger.
            """
            passenger = layout[row][column]

            # Check if the passenger has reached their seat row
            if passenger.seat.number != row + 1:
                # Move the passenger forward in the aisle
                if layout[row + 1][column] == '|':
                    layout[row + 1][column] = passenger
                    layout[row][column] = '|'
            else:
                # Handle baggage or movement to the target seat
                if passenger.has_baggage:
                    passenger.drop_off_baggage()  # Drop off baggage if applicable
                else:
                    offset = -1 if layout[-1].index(passenger.seat.letter) < column else 1
                    target_column = column + offset
                    target_seat = layout[row][target_column]
                    
                    # Handle the target seat being empty or occupied
                    if isinstance(target_seat, Seat):
                        layout[row][target_column] = (passenger, target_seat)
                    else:
                        seated_passenger = target_seat[0]
                        target_seat = target_seat[1]
                        layout[row][target_column] = (passenger, seated_passenger, target_seat)
                    layout[row][column] = '|'

        def _passenger_non_aisle_case(layout, row, column):
            """
            Handles the movement of a passenger off the aisle to their seat.

            Args:
                layout (list): The aircraft's seating layout.
                row (int): The current row of the passenger.
                column (int): The current column of the passenger.
            """
            passenger, seat = layout[row][column][0], layout[row][column][-1]

            # Check if the passenger is at their seat
            if passenger.seat == seat:
                passenger.sit_down()  # Passenger sits down
                return
            
            # Move the passenger closer to their seat
            offset = -1 if layout[-1].index(passenger.seat.letter) < column else 1
            target_column = column + offset
            target_seat = layout[row][target_column]

            # Handle the target seat being empty or occupied
            if isinstance(target_seat, Seat):
                layout[row][target_column] = (passenger, target_seat)
            else:
                seated_passenger, target_seat = target_seat[0], target_seat[1]
                layout[row][target_column] = (passenger, seated_passenger, target_seat)
            
            # Update the current position of the passenger
            layout[row][column] = layout[row][column][1:] if len(layout[row][column]) > 2 else seat

        def _entry_point(layout, aisle_index, passengers):
            """
            Handles passengers entering the aircraft through the aisle.

            Args:
                layout (list): The aircraft's seating layout.
                aisle_index (int): The column index of the aisle.
                passengers (list): The list of passengers boarding.
            """
            if layout[0][aisle_index] == '|':
                layout[0][aisle_index] = passengers.pop(0)  # Place the passenger in the aisle

        # Simulate boarding from back to front
        for row in range(len(layout) - 2, -1, -1):  # Start from the last row
            for column in order:
                if isinstance(layout[row][column], Passenger) and column == order[-1]:  # If passenger is in the aisle
                    _passenger_aisle_case(layout, row, column)
                elif isinstance(layout[row][column], tuple) and not layout[row][column][0].is_seated:
                    _passenger_non_aisle_case(layout, row, column)

        if passengers:  # Handle remaining passengers entering the aircraft
            _entry_point(layout, order[-1], passengers)

    def get_passengers_by_aisle(self):
        """
        Groups passengers by the aisle closest to their seat.

        Returns:
            dict: A mapping of aisle indices to passengers near those aisles.
        """
        # Get the seats closest to each aisle
        aisle_seat_map = self._aircraft.get_closest_seats_for_each_aisle()
        passengers_by_aisle = {aisle: [] for aisle in aisle_seat_map}

        # Match passengers to their respective aisles
        for aisle, seats in aisle_seat_map.items():
            for seat in seats:
                for passenger in self._passengers:
                    if passenger.seat == seat:
                        passengers_by_aisle[aisle].append(passenger)

        return passengers_by_aisle

    def boarding_simulation(self, time_interval=0.5):
        """
        Simulates the boarding process of passengers onto the aircraft.
        """
        layout = tuple(tuple(row) for row in self._aircraft.layout)

        passengers_by_aisle = self.get_passengers_by_aisle()
        for aisle, passengers in passengers_by_aisle.items():
            random.shuffle(passengers)
        while any(not passenger.is_seated and passenger.seat for passenger in self._passengers):  # Verify if all passengers with seats are seated
            for aisle, seats in self._aircraft.get_closest_seats_for_each_aisle().items():
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
                self.boarding(order, passengers_by_aisle[aisle])
            self.display_boarding_simulation()
            time.sleep(time_interval)
        print("Boarding completed!")

    def display_boarding_simulation(self):
        """
        Displays the current state of the boarding simulation.
        """
        os.system('cls' if os.name == 'nt' else 'clear') 

        display_layout = [
            [
                emojize(':seat:') if isinstance(cell, Seat) 
                else emojize(':busts_in_silhouette:') if (isinstance(cell, tuple) and len(cell) == 3) 
                else emojize(":bust_in_silhouette:") if (isinstance(cell, tuple) and cell[0].is_seated) 
                else emojize(':men’s_room:') if (isinstance(cell, Passenger) or (isinstance(cell, tuple) and not cell[0].is_seated)) 
                else emojize(':cross_mark:') if cell == "|" 
                else cell
                for cell in row
            ]
            for row in self._aircraft.layout
        ]

        displayed_layout = [["|"] + row + ["|"] for row in display_layout]

        indentation = (20 - self._aircraft.columns - 2) * " "

        output = "\n".join([indentation + " ".join(line) for line in displayed_layout[:-1]])
        print(output)
