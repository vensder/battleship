class Map:
    def __init__(self, dimension):
        self.dimension = dimension

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        if dimension < 0:
            self.__dimension = -dimension
        elif dimension == 0:
            raise ValueError("No ships -- no battle!")
        else:
            self.__dimension = dimension
            
