<h1 align="center"> ✈️ Flight Boarding Simulation (Python - OOP)</h1>

## Project Overview

The objective of this project is to develop an object-oriented simulation of the boarding process for a flight. This simulation implements a robust class hierarchy to model the complex interactions between passengers, seats, and aircraft layout. The project aims to visualize the boarding process and optimize it for efficiency using OOP principles.

## Features

- **Passenger Management**:
  - Creation and management of passenger instances, including their baggage status and seat assignments.
  - Simulation of passengers boarding the aircraft and taking their seats.
  - Implementation of passenger behaviors through encapsulated methods.

- **Aircraft Layout**:
  - Generation of aircraft seating layouts with single or double aisles.
  - Management of seat assignments and tracking of available seats.
  - Flexible layout generation based on aircraft configuration.

- **Boarding Simulation**:
  - Visualization of the boarding process, including passengers moving through the aisles and taking their seats.
  - Optimization of boarding order to reduce boarding time.
  - Event-driven simulation using object interactions.

## Technology Stack

### Core Technologies
- **Programming Language**:
  - Python 3.x
  - Object-Oriented Programming (OOP) paradigm

### Project Architecture
- **Design Patterns**:
  - Factory Pattern for aircraft and seat creation
  - Observer Pattern for passenger state changes
  - Strategy Pattern for boarding algorithms

### Class Structure
- **Core Classes**:
  - `Aircraft`: Manages aircraft configuration and layout
  - `Flight`: Handles flight-specific operations and boarding process
  - `Passenger`: Represents individual passengers and their behaviors
  - `Seat`: Defines seat properties and states

### Dependencies
- **Libraries**:
  - `emoji`: For visual representation of the boarding process
  - `uuid`: For unique passenger identification
  - `copy`: For deep copying of objects
  - `random`: For simulation randomization

## Project Structure

```
📦FlightSimulation
 ┣ 📂src
 ┃ ┣ 📂models
 ┃ ┃ ┣ 🐍aircraft.py
 ┃ ┃ ┣ 🐍flight.py 
 ┃ ┃ ┣ 🐍passenger.py
 ┃ ┃ ┗ 🐍seat.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 🐍display.py
 ┃ ┃ ┗🐍run.py
 ┃ ┗🐍main.py
 ┣ 📜README.md
 ┣ 📜LICENSE
 ┗ 📜requirements.txt
```

## Object-Oriented Design

The project implements a clean object-oriented architecture with the following key principles:

- **Encapsulation**: All classes use private attributes with public property decorators
- **Inheritance**: Extensible class hierarchy for different aircraft types
- **Polymorphism**: Flexible boarding strategies through common interfaces
- **Abstraction**: Clear separation of concerns between classes

## Setup

### Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.x** to run the simulation
- **pip** to install required libraries

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/MrPaquiteau/flight-boarding-simulation.git
cd flight-boarding-simulation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Simulation
Execute the main.py script to start the boarding simulation:

```bash
python src/main.py
```

## Usage

The simulation provides an object-oriented approach to modeling aircraft boarding:

```python
# Create an aircraft instance
aircraft = Aircraft(rows=20, columns=8)

# Initialize a flight
flight = Flight(aircraft)

# Launch the simulation
flight.boarding_simulation()
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
