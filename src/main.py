from models.flight import Flight
from models.aircraft import Aircraft
from utils.run import simulation

def main():
    rows = 10
    columns = 10
    aircraft = Aircraft(rows, columns)

    flight = Flight(aircraft)

    simulation(flight)

if __name__ == "__main__":
    main()