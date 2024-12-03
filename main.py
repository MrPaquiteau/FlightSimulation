from models.flight import Flight
from models.aircraft import Aircraft

def main():
    rows = 10
    columns = 10
    aircraft = Aircraft(rows, columns)

    flight = Flight(aircraft)
    flight.boarding_simulation()

if __name__ == "__main__":
    main()