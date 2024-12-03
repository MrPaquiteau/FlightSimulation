import uuid

class Passenger:
    """"
    Represents a passenger on a flight.

    Attributes (Properties):
    - identifier (str): The unique identifier of the passenger
    - has_baggage (bool): Indicates whether the passenger has baggage
    - seat (Seat): The seat assigned to the passenger, if any
    - is_seated (bool): Indicates whether the passenger is currently seated

    Methods:
    - sit_down(): Marks the passenger as seated
    - stand_up(): Marks the passenger as standing
    - drop_off_baggage(): Simulates baggage drop-off by setting has_baggage to False
    - remove_passenger(passenger_id): Class method to remove a Passenger instance from the class's list by its identifier
    """

    # Class attribute to maintain a list of all created Passenger instances
    passengers = []

    # Constructor method to initialize a Passenger object
    def __init__(self, flight, has_baggage: bool):
        """
        Initialize a Passenger instance.

        :param flight: The flight this passenger is associated with
        :param has_baggage: Boolean indicating if the passenger has baggage
        """
        self._id = str(uuid.uuid4())
        self._flight = flight
        self._has_baggage = has_baggage
        self._seat = None
        self._is_seated = False
        Passenger.passengers.append(self)
        flight._passengers.append(self)

    # Property to access the passenger's unique identifier
    @property
    def identifier(self):
        """Return the unique identifier of the passenger."""
        return self._id

    # Property to access and modify the passenger's baggage status
    @property
    def has_baggage(self):
        """Return whether the passenger has baggage."""
        return self._has_baggage

    @has_baggage.setter
    def has_baggage(self, new_value: bool):
        """Set the baggage status of the passenger."""
        self._has_baggage = new_value

    # Property to access and modify the passenger's seat assignment
    @property
    def seat(self):
        """Return the seat assigned to the passenger, if any."""
        return self._seat

    @seat.setter
    def seat(self, new_value):
        """Assign a new seat to the passenger."""
        self._seat = new_value

    # Property to access the passenger's seated status
    @property
    def is_seated(self):
        """Return whether the passenger is currently seated."""
        return self._is_seated

    # Method to mark the passenger as seated
    def sit_down(self):
        """Mark the passenger as seated."""
        self._is_seated = True

    # Method to mark the passenger as standing
    def stand_up(self):
        """Mark the passenger as standing."""
        self._is_seated = False

    # Method to handle baggage drop-off (sets has_baggage to False)
    def drop_off_baggage(self):
        """Simulate baggage drop-off by setting has_baggage to False."""
        self.has_baggage = False

    # Class method to remove a Passenger instance from the class's list by its identifier
    @classmethod
    def remove_passenger(cls, passenger_id):
        """
        Remove a Passenger instance from the class's list by its identifier.

        :param passenger_id: The unique identifier of the passenger to remove
        """
        passenger = cls.get_passenger_by_id(passenger_id)
        if passenger:
            cls.passengers.remove(passenger)

    # String representation of the Passenger instance for printing
    def __repr__(self):
        """Return a string representation of the Passenger instance."""
        return f"Passenger({self._id})"