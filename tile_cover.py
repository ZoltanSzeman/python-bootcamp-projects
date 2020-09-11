# Created by Zoltan Szeman
# Task: Calculate the number of tiles needed to cover w x h area.
    
class Tile:
    """A class object for tile cover represantation"""
    def __init__(self, a, b, cost):
        """Sides and cost attributes of a single tile"""
        self.a = a
        self.b = b
        self.area = a * b
        self.cost = cost
    
    def total_no(self, cover_area):
        """Returns the total number of tiles"""
        if cover_area % self.area == 0:
            return cover_area // self.area
        else:
            return cover_area // self.area + 1
            
    def total_cost(self, cover_area):
        """Returns the total cost of tiles"""
        return self.total_no(cover_area) * self.cost

# Area is in cm^2, cost is in HUF
w = 330 #cm
h = 420 #cm
cover_area = w * h #cm^2
a = 30 #cm
b = 30 #cm
cost = 1599 #HUF
tile = Tile(a, b, cost)

print(f'To cover {w} x {h} area you need {tile.total_no(cover_area)} tiles '
            f'costing {tile.total_cost(cover_area)} HUF')
