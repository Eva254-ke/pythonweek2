# Activity 1: Device and Smartphone Classes
class Device:
    """
    Base class representing a general electronic device.
    """
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price  # Encapsulation: private attribute

    # Getter for price
    def get_price(self):
        return self._price

    # Setter for price with validation
    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self._price = new_price

    def display_details(self):
        """
        Display device details.
        """
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self._price:.2f}"


class Smartphone(Device):
    """
    Subclass representing a Smartphone, inheriting from Device.
    """
    def __init__(self, brand, model, price, os, camera_megapixels, battery_capacity):
        super().__init__(brand, model, price)  # Initialize base class attributes
        self.os = os
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def take_photo(self):
        """
        Simulate taking a photo.
        """
        return f"Taking a photo with {self.camera_megapixels} MP camera."

    def install_app(self, app_name):
        """
        Simulate app installation.
        """
        return f"Installing {app_name} on {self.model} running {self.os}."

    # Polymorphism: Override display_details method
    def display_details(self):
        """
        Display smartphone-specific details, overriding parent method.
        """
        base_details = super().display_details()
        return (f"{base_details}\nOS: {self.os}, Camera: {self.camera_megapixels} MP, "
                f"Battery: {self.battery_capacity} mAh")


# Activity 2: Vehicles with Polymorphism
class Vehicle:
    """
    Base class for vehicles.
    """
    def move(self):
        """
        Placeholder method for movement. 
        To be overridden in derived classes.
        """
        raise NotImplementedError("Subclasses must override the move() method.")


class Car(Vehicle):
    """
    A car moves by driving.
    """
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    """
    A plane moves by flying.
    """
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    """
    A boat moves by sailing.
    """
    def move(self):
        return "Sailing 🛥️"


# Combined Execution
if __name__ == "__main__":
    # Activity 1: Device and Smartphone Example
    device = Device("GenericBrand", "ModelX", 299.99)
    smartphone = Smartphone("TechBrand", "SuperPhone", 999.99, "Android", 108, 5000)

    device.set_price(350)
    print(device.display_details())
    print(smartphone.display_details())
    print(smartphone.take_photo())
    print(smartphone.install_app("ChatGPT"))

    print("\n--- Polymorphism with Vehicles ---")
    # Activity 2: Polymorphism with Vehicles
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())
