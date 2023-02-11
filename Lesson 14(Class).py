"""2. Implement previous method with magic method"""

class Country:
    def __init__(self, name, population) -> None:
        self.name = name
        self.population = population

    def __add__(self, fuseCountry):
        return Country(self.name + " " + fuseCountry.name, self.population + fuseCountry.population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

first_country = bosnia
second_country = herzegovina
fused_country = first_country + second_country
print(fused_country.name, fused_country.population)
print(fused_country.name)
print(fused_country.population)
"""1. Create add method to add two countries together. This method should create another
country object with the name of the two countries combined and
population of the two countries added together"""


class Country:
    def __init__(self, name, population) -> None:
        self.name = name
        self.population = population


    def add(self, country):
        name = self.name + " " + country.name
        population = self.population + country.population
        return Country(name, population)



bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)

"""3. Create a Car class with the following attributes: brand, model, year, and speed.
The Car class should have the following methods: accelerate and brake.
The accelerate method should increase the speed by 5,
and the brake method should decrease the speed by 5."""

class Car:
    def __init__(self, brand, model, year, speed) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        return int(self.speed + 5)

    def brake(self):
        if self.speed < 0:
            return "Speed can not be lower than 0"
        if self.speed > 250:
            return "The car can't move faster!"
        return int(self.speed - 5)

sport_car = Car("ferrari", "f5", 2020, 150)
print(sport_car.accelerate())
print(sport_car.brake())


"""Create a Robot class with the following attributes: orientation, position_x, position_y. 
The Robot class should have the following methods: move, turn, and display_position. 
The move method should take a number of steps and move the robot in the direction it is 
currently facing. The turn method should take a direction (left or right) 
and turn the robot in that direction. 
The display_position method should print the current position of the robot."""

class Robot:
    def __init__(self, orientation=90, position_x=0, position_y=0) -> None:
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, num_of_steps):
        self.position_y += num_of_steps
        self.position_x += num_of_steps

    def turn(self, direction):
        if direction == "right":
            self.orientation += 90
        if direction == "left":
            self.orientation -= 90

    def display(self):
        return f"The Robot is directed on {self.orientation} degree. He made {self.position_y}" \
               f" steps on Y and {self.position_x} on X"


antony = Robot(90, 10, 10)
antony.turn("right")
antony.turn("right")
antony.move(20)
print(antony.display())
antony.turn("left")
antony.move(30)
print(antony.display())


