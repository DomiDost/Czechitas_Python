import math

class Locality:
    def __init__(self, name, locality_coefficent):
        self.name = name
        self.locality_coefficient = locality_coefficent

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality


class Estate (Property):
    def __init__(self, locality:Locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        if self.estate_type == "land":
            return math.ceil(self.area * 0.85 * self.locality.locality_coefficient)
        if self.estate_type == "building site":
            return math.ceil(self.area * 9 * self.locality.locality_coefficient)
        if self.estate_type == "forest":  # Fixed spelling from 'forrest'
            return  math.ceil(self.area * 0.35 * self.locality.locality_coefficient)
        if self.estate_type == "garden":
            return  math.ceil(self.area * 2 * self.locality.locality_coefficient)

# Test case
#locality_test = Locality("Test Location", 2)
#estate_test = Estate(locality_test, "forest", 465)
#print("Expected tax: 350")
#print("Calculated tax:", estate_test.calculate_tax())

class Residence(Property):
    def __init__(self, locality:Locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.commercial:#True value - multiply twice the value
            return math.ceil(self.area * self.locality.locality_coefficient *15*2)
        return math.ceil(self.area * self.locality.locality_coefficient *15)
        
# Test case
locality_test = Locality("Test Location", 3)
residence_test = Residence(locality_test, 60, False)
print("Expected tax: 2700")
print("Calculated tax:", residence_test.calculate_tax())




