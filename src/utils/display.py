from emoji import emojize
from models.seat import Seat
from models.passenger import Passenger

def display_simulation(flight, round):
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
        for row in flight._aircraft.layout
    ]

    displayed_layout = [["|"] + row + ["|"] for row in display_layout]

    indentation = (20 - flight._aircraft.columns - 2) * " "

    print('Round', round)
    for ligne in displayed_layout[:-1]:
        print(indentation + " ".join(ligne))
    print('\n')