from box import Box

class Product(Box):


    def __init__(self, name, large, width, height):
        super().__init__(name, large, width, height)

    def determinate_total_volume(self, products_number):
        return self.volume * products_number
