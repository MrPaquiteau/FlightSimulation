
class Seat:
    """
    Represents an individual seat on an aircraft.
    
    Attributes (Properties):
    - letter (str): The letter designation of the seat (e.g., 'A', 'B', etc.)
    - number (int): The numerical designation of the seat
    - coordinates (tuple): A tuple containing the letter and number for quick reference
    - name (str): A concatenated string of the letter and number for a human-readable name
    - aircraft (Aircraft): The aircraft to which this seat belongs
    """

    def __init__(self, letter: str, number: int, aircraft):
        """
        Initializes a Seat instance.
        
        Parameters:
        - letter (str): Seat letter designation
        - number (int): Seat number designation
        - aircraft (Aircraft): The aircraft this seat is part of
        """
        self._letter = letter  # Internal storage for the seat's letter
        self._number = number  # Internal storage for the seat's number
        self._coordinates = (letter, number)  # Quick reference tuple
        self._name = f"{letter}{number}"  # Human-readable name
        self._aircraft = aircraft  # Reference to the parent aircraft
        # Automatically adds this seat to the aircraft's seat list
        aircraft.add_seat(self)

    # Property for controlled access to the seat's letter
    @property
    def letter(self):
        return self._letter

    # Property for controlled access to the seat's number
    @property
    def number(self):
        return self._number

    # Property for controlled access to the seat's coordinates
    @property
    def coordinates(self):
        return self._coordinates

    # Property for controlled access to the seat's name
    @property
    def name(self):
        return self._name

    # Property for controlled access to the parent aircraft
    @property
    def aircraft(self):
        return self._aircraft

    # Custom representation of the Seat instance for debugging/logging
    def __repr__(self):
        return f"Seat({self._name})"