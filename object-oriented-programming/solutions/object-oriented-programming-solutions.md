# OOP Exercises

## Part 1

1. Create a `Vehicle` class without any attribute and methods.

    ```py
    class Vehicle:
        pass
    ```

2. Extend the `Vehicle` class to contain attributes for max speed and colour. Instantiate the class and print out the attributes.

    ```py
    class Vehicle:
        def __init__(self, max_speed, colour):
            self.max_speed = max_speed
            self.colour = colour

    vehicle = Vehicle(150, 'red')
    print(vehicle.max_speed, vehicle.colour)
    ```

3. Extend the `Vehicle` class to contain methods for the below. Instantiate the class and call the two methods to update the attributes. Print the changes out.
    - Change the value of max speed
    - Change the car colour

    ```py
    class Vehicle:
        def __init__(self, max_speed, colour):
            self.max_speed = max_speed
            self.colour = colour

        def update_max_speed(self, new_value):
            self.max_speed = new_value

        def update_colour(self, new_colour):
            self.colour = new_colour

    vehicle = Vehicle(150, 'red')
    print(vehicle.max_speed, vehicle.colour)

    vehicle.update_max_speed(50)
    vehicle.update_colour('blue')
    print(vehicle.max_speed, vehicle.colour)
    ```

## Part 2

1. Create a child class `Bus` that will inherit all of the variables and methods of the Vehicle class and nothing else. Instantiate a `Bus` instance and print out the attributes.

    ```py
    class Bus(Vehicle):
        pass

    bus = Bus()
    print(bus.max_speed, bus.colour)
    ```

2. Use one of the built-in Python functions to print out the underlying object type of the `Bus` object.

    ```py
    bus = Bus()
    print(type(bus))

    # <class '__main__.Bus'>
    ```

3. Use one of the built-in Python functions to print out if the `Bus` object is an instance of `Vehicle`.

    ```py
    bus = Bus()
    print(isinstance(bus, Vehicle))

    # True
    ```

4. Extend the `Bus` class to also contain an attribute of `seating_capacity`. Add a method to calculate the price of a ticket. This is calculated as `seating_capacity * 0.05`, with an extra 10% of the total of `seating_capacity * 0.05` on top. Instantiate a `Bus` instance and print the ticket price.

    ```py
    class Bus(Vehicle):
        def __init__(self, max_speed, colour, seating_capacity):
            super().__init__(max_speed, colour)
            self.seating_capacity = seating_capacity
            
        def calculate_ticket_price(self):
            initial_price = self.seating_capacity * 0.05
            return initial_price + (10 / 100)
        
    bus = Bus(40, 'Yellow', 80)
    print(bus.calculate_ticket_price())
    ```

5. Research how to print a `Bus` object in a printable representation. Hint: Look up overriding the `__str__` function. It should print something like `Bus: Max speed: 120, Colour: white, Seating capacity: 40`.

    ```py
    class Bus(Vehicle):
        def __init__(self, max_speed, colour, seating_capacity):
            super().__init__(max_speed, colour)
            self.seating_capacity = seating_capacity
            
        def calculate_ticket_price(self):
            initial_price = self.seating_capacity * 0.05
            return initial_price * 1.1
        
        def __str__(self):
            return f'Bus: Max speed: {self.max_speed}, Colour: {self.colour}, Seating capacity: {self.seating_capacity}'
        
    bus = Bus(120, 'white', 40)
    print(bus)

    # 'Bus: Max speed: 120, Colour: white, Seating capacity: 40'
    ```
