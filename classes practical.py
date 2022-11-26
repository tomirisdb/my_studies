import inspect


class House:
    def __init__(self, name, number_of_tenants, number_of_rooms):
        self.name = name
        self.tenants = number_of_tenants
        self.rooms = number_of_rooms

    def show_street(self):
        print(f'{self.name} name of the street')

    def show_people(self):
        print(f'{self.tenants} the number of tenants')

    def show_rooms(self):
        print(f'{self.rooms} the number of rooms')

    def change_tenants(self, addtenants):
        """This function changes number of tenants"""
        self.tenants += addtenants
        if self.tenants > self.rooms:
            print('too many tenants ')
            self.tenants -= addtenants



house = House('Sims Drive', 4, 5)
print(house.name)
print(house.rooms)
print(house.tenants)
house.change_tenants(1)
print(house.tenants)
print(inspect.getsource(house.change_tenants))


print(f'this house is located on {house.name}, in this house live {house.tenants}, the number of rooms is {house.rooms}')

