from .seat import Seat  # Importing the Seat class (assumed to handle individual seat details)

class Aircraft:
    """
    A class to represent an aircraft, including its seating layout, capacity, and seat management.
    """
    
    def __init__(self, rows: int, columns: int):
        """
        Initializes an Aircraft object.

        Args:
            rows (int): The number of rows in the aircraft.
            columns (int): The number of columns in the aircraft.
        """
        self._rows = rows  # Number of rows in the aircraft
        self._columns = columns  # Number of columns in the aircraft
        self._capacity = rows * columns  # Total capacity (rows * columns)
        self._layout = []  # Holds the seating layout (list of lists)
        self._seats = []  # Holds the list of added Seat objects
        self.generate_layout()  # Generate the initial layout based on rows and columns

    # Getter and setter for rows
    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, new_val: int):
        self._rows = new_val

    # Getter and setter for columns
    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, new_val: int):
        self._columns = new_val

    # Getter for capacity (no setter as capacity is derived from rows and columns)
    @property
    def capacity(self):
        return self._capacity

    # Getter for layout
    @property
    def layout(self):
        return self._layout

    # Getter for seats
    @property
    def seats(self):
        return self._seats

    def add_seat(self, seat):
        """
        Adds a Seat object to the list of seats.

        Args:
            seat (Seat): The seat to add.
        """
        self._seats.append(seat)

    def _generate_single_aisle_layout(self, labels: list):
        """
        Generates a single-aisle seating layout.

        Args:
            labels (list): A list of column labels (e.g., ['A', 'B', ...]).

        Returns:
            list: The seating layout including an aisle separator.
        """
        num_columns = self.columns
        # Create seats for each row and column
        layout = [
            [Seat(labels[j], i + 1, self) for j in range(num_columns)]
            for i in range(self.rows)
        ]
        aisle_index = num_columns // 2  # Determine where the aisle is placed
        # Insert aisle in each row
        for row in layout:
            row.insert(aisle_index, "|")
        labels.insert(aisle_index, "-")  # Add aisle marker to the labels
        layout.append(labels)  # Append the labels to the layout for reference
        return layout

    def _generate_double_aisle_layout(self, labels: list):
        """
        Generates a double-aisle seating layout.

        Args:
            labels (list): A list of column labels (e.g., ['A', 'B', ...]).

        Returns:
            list: The seating layout including two aisle separators.
        """
        layout = [
            [Seat(labels[j], i + 1, self) for j in range(self.columns)]
            for i in range(self.rows)
        ]
        aisle_index = self.columns // 3  # Determine where the aisles are placed
        # Insert aisles in each row
        for row in layout:
            row.insert(aisle_index, "|")
            row.insert(-aisle_index, "|")
        labels.insert(aisle_index, "-")  # Add markers for the first aisle
        labels.insert(-aisle_index, "-")  # Add markers for the second aisle
        layout.append(labels)  # Append the labels to the layout for reference
        return layout

    def generate_layout(self):
        """
        Generates the seating layout based on the number of columns.
        Uses single-aisle for <=6 columns and double-aisle for more.
        """
        labels = [chr(65 + i) for i in range(self.columns)]  # Generate column labels (e.g., A, B, C...)
        if self.columns <= 6:
            # Use single-aisle layout for narrow planes
            layout = self._generate_single_aisle_layout(labels)
        else:
            # Use double-aisle layout for wider planes
            layout = self._generate_double_aisle_layout(labels)
        self._layout = layout  # Store the generated layout

    def get_closest_seats_for_each_aisle(self):
        """
        Finds the closest seats to each aisle and groups them.

        Returns:
            dict: A mapping of aisle positions (column indices) to the closest seats.
        """
        # Find the positions of aisles based on the layout labels
        aisle_positions = [index for index, label in enumerate(self._layout[-1]) if label == "-"]
        aisle_seat_map = {aisle: [] for aisle in aisle_positions}  # Initialize aisle-to-seat map

        # Iterate through each seat to find its closest aisle
        for seat in self._seats:
            seat_row = seat.number - 1  # Determine the seat's row
            seat_col = self._layout[-1].index(seat.letter)  # Determine the seat's column
            # Find the closest aisle to the current seat
            closest_aisle = min(aisle_positions, key=lambda aisle: abs(aisle - seat_col))
            aisle_seat_map[closest_aisle].append(seat)  # Map the seat to the closest aisle

        return aisle_seat_map
