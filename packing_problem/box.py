class Box:


    def __init__(self, name, large, width, height):
        self.name = name
        self.large = large
        self.width = width
        self.height = height
        self.volume = self.large * self.width * self.height
