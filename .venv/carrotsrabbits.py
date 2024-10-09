# Import necessary libraries and functions
import Lib.ketlib
import random
from Lib.ketlib import try_string

# Function to check if a rabbit has died due to starvation
def deathCheck(f1):
    # If the rabbit's total hunger exceeds 60, it dies from starvation
    if f1.total_hunger > 60:
        print("Unfortunately the rabbit died from starvation")
        return True
    return False

# Rabbit class to represent a rabbit's attributes and eating behavior
class Rabbit():
    def __init__(self):
        # Each rabbit has a random mouth size (3 to 8) that affects the size of carrots it can eat
        self.mouth_size = random.randint(3, 8)
        # Each rabbit starts with a random hunger level (40 to 60)
        self.total_hunger = random.randint(40, 60)
        self.is_hungry = True  # Determines if the rabbit is hungry
        self.carrots_eaten = 0  # Tracks how many carrots the rabbit has eaten
        self.energy = random.randint(1, 3)  # Represents the number of attempts the rabbit can make before stopping

    # Method for the rabbit to eat a carrot
    def eat(self, carrot):
        if self.is_hungry:  # Only eats if the rabbit is hungry
            if carrot.weight < self.mouth_size:  # Checks if the carrot is small enough to eat
                self.total_hunger -= carrot.weight  # Reduces hunger based on carrot's weight
                print(f"The rabbit ate the carrot weighing {carrot.weight} and now has a total remaining hunger of "
                      f"{self.total_hunger}")
                carrot.weight = 0  # Carrot is fully eaten
                self.carrots_eaten += 1  # Increment the count of carrots eaten
                if self.total_hunger <= 0:  # If the rabbit is full or overate
                    self.is_hungry = False  # Rabbit is no longer hungry
                    print(f"Your rabbit had a remaining hunger of {self.total_hunger} and ate "
                          f"{self.carrots_eaten} carrots")
                    if self.total_hunger <= -1:  # If the rabbit ate too much
                        print("Unfortunately the rabbit over ate and died :)")
            elif carrot.weight >= self.mouth_size:  # If the carrot is too big
                print("The carrot is unfortunately too big for the rabbit's mouth")
                self.total_hunger += 1  # Slight hunger increase for failed attempts
        else:
            print("Unfortunately the rabbit is no longer hungry")  # Rabbit is already full

# Carrot class to represent each carrot in the field
class Carrot():
    def __init__(self):
        self.weight = random.randint(1, 7)  # Each carrot has a random weight between 1 and 7

# Main function that sets up the simulation
def main():
    # Create a random-sized carrot field (rows x columns)
    carrot_land_rowsY = random.randint(4, 8)
    carrot_land_rowsX = random.randint(4, 8)
    num_carrots = carrot_land_rowsX * carrot_land_rowsY  # Total number of carrots
    num_rabbits = random.randint(2, 4)  # Randomly decide the number of rabbits (between 2 and 4)

    # Create a list of Rabbit and Carrot objects
    rabbits = [Rabbit() for _ in range(num_rabbits)]
    carrots = [Carrot() for _ in range(num_carrots)]

    # Loop continues while there are hungry rabbits and uneaten carrots
    while any(r.is_hungry for r in rabbits) and any(carrot.weight > 0 for carrot in carrots):
        for rabbit in rabbits:
            if rabbit.is_hungry:
                attempts = 0  # Number of attempts the rabbit makes to eat
                while attempts <= rabbit.energy:
                    # Get the list of available carrots (carrots with weight > 0)
                    available_carrots = [carrot for carrot in carrots if carrot.weight > 0]
                    if not available_carrots:  # If no carrots are available
                        print("Unfortunately the rabbit could not find any carrots")
                        rabbit.total_hunger += 1  # Slight hunger increase for failed attempts

                    # Select a random carrot from the available ones
                    selected_carrot = random.choice(available_carrots)
                    rabbit.eat(selected_carrot)  # Rabbit tries to eat the carrot
                    attempts += 1  # Increment the number of attempts

                    if not rabbit.is_hungry:  # If the rabbit is no longer hungry, stop attempting
                        break
                    rabbits_to_remove = []  # List to hold rabbits that die
                    if deathCheck(rabbit):  # Check if the rabbit dies due to hunger
                        rabbits_to_remove.append(rabbit)  # Add the rabbit to removal list if it dies
            for rabbit in rabbits_to_remove:  # Remove any dead rabbits from the list
                rabbits.remove(rabbit)

# Run the simulation
main()
