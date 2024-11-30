from box import Box

class Container(Box):


    def __init__(self, name, large, width, height):
        super().__init__(name, large, width, height)

    def can_package_products(self, products_total_volume):
        return self.volume >= products_total_volume
