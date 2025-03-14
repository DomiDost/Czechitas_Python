import math
from abc import ABC, abstractmethod
from enum import Enum


class Locality:
    def __init__(self, name, locality_coefficent):
        self.name = name
        self.locality_coefficient = locality_coefficent


class Property(ABC):  
    def __init__(self, locality):
        self.locality = locality

class Estate_type(Enum):
    land = 0.85
    building_site = 9
    forest = 0.35
    garden = 2


class Estate (Property):
    def __init__(self, locality:Locality, estate_type: Estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        if self.estate_type == Estate_type.land:
            return math.ceil(self.area * 0.85 * self.locality.locality_coefficient)
        if self.estate_type == Estate_type.building_site:
            return math.ceil(self.area * 9 * self.locality.locality_coefficient)
        if self.estate_type == Estate_type.forest: 
            return  math.ceil(self.area * 0.35 * self.locality.locality_coefficient)
        if self.estate_type == Estate_type.garden:
            return  math.ceil(self.area * 2 * self.locality.locality_coefficient)
        return 0
    
    def __str__(self):
        if self.estate_type == Estate_type.land:
            return f"Zemědelský pozemek, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        if self.estate_type == Estate_type.building_site:
            return f"Stavebný pozemek, lokalita {self.locality.name} (koeficient{self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        if self.estate_type ==  Estate_type.forest:
            return f"Les, lokalita {self.locality.name} (koeficient{self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        if self.estate_type == Estate_type.garden:
            return f"Záhrada, lokalita {self.locality.name} (koeficient{self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

# Test case
#locality_test = Locality("Manětín", 1)
#estate_test = Estate(locality_test, "land", 900)
#print("Expected text: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, daň 765 Kč.")
#print(estate_test) #print the formatted string

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
#locality_test = Locality("Test Location", 3)
#residence_test = Residence(locality_test, 60, False)
#print("Expected tax: 2700")
#print("Calculated tax:", residence_test.calculate_tax())

class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []
    def add_property(self, property_obj:Property):
        self.property_list.append(property_obj)
    def calculate_tax(self):
        total_tax = 0
        for property_obj in self.property_list:
            total_tax = total_tax + property_obj.calculate_tax()
        return total_tax
    def __str__(self):
        return f"Daňové přiznání {self.name}, obsahuje {len(self.property_list)} položky a výška daně je {self.calculate_tax()}.  "



#Test of code
# Create Locality
locality_test = Locality("Praha", 2)

# Create Estates
estate_1 = Estate(locality_test, Estate_type.forest, 500)  # Expected tax: 500 * 0.35 * 2 = 350
estate_2 = Estate(locality_test, Estate_type.land, 1000)   # Expected tax: 1000 * 0.85 * 2 = 1700

# Create Residence
residence_1 = Residence(locality_test, 60, False)  # Expected tax: 60 * 2 * 15 = 1800

# Create TaxReport
tax_report = TaxReport("Pán Novák")

# Add properties to the report
tax_report.add_property(estate_1)
tax_report.add_property(estate_2)
tax_report.add_property(residence_1)

# Expected total tax calculation
expected_total_tax = 350 + 1700 + 1800  # 3850

# Print results
print(tax_report)

# Additional check
print(f"Expected total tax: {expected_total_tax}")
print(f"Calculated total tax: {tax_report.calculate_tax()}")

# Assertion to check correctness
assert tax_report.calculate_tax() == expected_total_tax, "Tax calculation is incorrect!"
print("✅ Tax calculation works correctly!")
