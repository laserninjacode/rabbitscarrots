import random
# TODO


# Klassen Rabbit som representerar en kanin
class Rabbit():
    def __init__(self):
        self.mouth_size = random.randint(5, 8)  # Munstorlek mellan 5 och 8
        self.total_hunger = random.randint(40, 60)  # Hunger mellan 40 och 60
        self.is_hungry = True
        self.is_alive = True
        self.carrots_eaten = 0
        self.energy = random.randint(1, 3)  # Energinivå mellan 1 och 3

    def eat(self, carrot):
        if self.is_hungry and self.is_alive:
            if carrot.weight < self.mouth_size:  # Kaninen kan äta moroten
                self.total_hunger -= carrot.weight
                print(f"The rabbit ate the carrot weighing {carrot.weight} "
                      f"and now has a total remaining hunger of {self.total_hunger}")
                carrot.weight = 0  # Moroten är nu uppäten
                self.carrots_eaten += 1
                if self.total_hunger <= 0:
                    self.is_hungry = False
                    print(f"Your rabbit had a remaining hunger of {self.total_hunger} "
                          f"and ate {self.carrots_eaten} carrots")
                    if self.total_hunger <= -1:
                        print("Unfortunately the rabbit overate and died :)")
                        self.is_alive = False
            else:  # Moroten är för stor
                print("The carrot is unfortunately too big for the rabbit's mouth")
                self.total_hunger += 1

            if self.total_hunger > 60:  # Dör av hunger
                print("The rabbit died of starvation")
                self.is_alive = False

# Klassen Carrot som representerar en morot
class Carrot():
    def __init__(self):
        self.weight = random.randint(3, 6)  # Morotens vikt mellan 3 och 6

# Huvudfunktionen för simuleringen
def main():
    carrot_land_rowsY = random.randint(6, 10)
    carrot_land_rowsX = random.randint(6, 10)
    num_carrots = carrot_land_rowsX * carrot_land_rowsY
    num_rabbits = random.randint(2, 4)
    print(f"Number of rabbits at start: {num_rabbits}")

    rabbits = [Rabbit() for _ in range(num_rabbits)]
    carrots = [Carrot() for _ in range(num_carrots)]

    while any(r.is_hungry for r in rabbits) and any(carrot.weight > 0 for carrot in carrots):

        for rabbit in rabbits:
            if rabbit.is_hungry and rabbit.is_alive:
                attempts = 0
                while attempts <= rabbit.energy:
                    available_carrots = [carrot for carrot in carrots if carrot.weight > 0]
                    if not available_carrots:
                        print("Unfortunately the rabbit could not find any carrots")
                        rabbit.total_hunger += 1
                        break

                    selected_carrot = random.choice(available_carrots)
                    rabbit.eat(selected_carrot)
                    attempts += 1

                    if not rabbit.is_hungry:
                        break

            rabbits_to_remove = []  # Hålla koll på döda kaniner
            if not rabbit.is_alive:
                rabbits_to_remove.append(rabbit)

            # Ta bort döda kaniner efter varje loop
            for rabbit in rabbits_to_remove:
                if rabbit in rabbits:
                    rabbits.remove(rabbit)
                    num_rabbits -= 1

            if not rabbits:
                break  # Avbryt om inga kaniner är kvar

    print("No hungry more rabbits left, bye bye"
          f"\nA total of {num_rabbits} rabbits survived")  # Skriv ut meddelande när alla kaniner är döda eller mätta

# Kör simuleringen
main()
