import random

from car import Car

# Constants
START_MD = 5                    # Our car-field's starting movement
MOVE_INC = 10                   # The increment by which our cars will speed up.


class CarManager:
    """
    Creation of a car field. Car objects will be created in our car field and will move
    across the screen as one-unit. Player object will need to traverse the screen without
    colliding into any object on the car field. Car objects will progressively move
    faster across the screen as player reaches higher levels.

     This class has built-in methods for the following:
    - Creating a car on the field.
    - Moving the car field across the screen.
    - Leveling up the difficulty of the cars.
    """

    def __init__(self):
        # This is an array of car objects that initializes to empty.
        self.all_cars = []
        self.car_speed = START_MD

    def create_car(self):
        """
        Creates a randomly colored car at a random y-coordinate on the screen. Appends
        this car object to our car field.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Moves each car in the car array (field) at a specified speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        Gradually makes the speed of our car field faster.
        """
        self.car_speed += MOVE_INC
