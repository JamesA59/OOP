# Property 6

class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        return self._x
    
    @value.setter
    def value(self, val):
        self._x = val

    # Deleter method specifies what happens when a property is deleted
    @value.deleter
    def value(self):
        print('value deleted')

p = Product(12,24)

# Deletes a value and prints 'value deleted' in terminal
del p.value