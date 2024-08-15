import math

class formula:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi = math.pi
        self.water_density = 1000 # Unit: kg/m^3

    def maximum_volume(self):
        max_vol=self.pi * self.radius**2 * self.height #Formula for calculating maximum vlume
        return max_vol

    def mass_of_water(self):
        water_mass=self.maximum_volume() * self.water_density #Formula for calculating water mass
        return water_mass
