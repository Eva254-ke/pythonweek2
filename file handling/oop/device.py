
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


# Example Usage
# Creating objects for testing purposes
device = Device("GenericBrand", "ModelX", 299.99)
smartphone = Smartphone("TechBrand", "SuperPhone", 999.99, "Android", 108, 5000)

# Test Encapsulation
device.set_price(350)
device.set_price(-20)  # Invalid price

# Display details of each object
device_details = device.display_details()
smartphone_details = smartphone.display_details()

# Smartphone specific features
photo_action = smartphone.take_photo()
app_installation = smartphone.install_app("ChatGPT")

print(device_details)
print(smartphone_details)
print(photo_action)
print(app_installation)
