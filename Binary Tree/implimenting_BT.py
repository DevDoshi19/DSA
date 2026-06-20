"""
         drink
        /     \
      hot      cold
    /   \       /  \
 tea  coffee cola  fanta

"""

class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

drink = Node("drink")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta= Node("fanta")

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

drink.left = hot
drink.right = cold

print(drink.data)  # should be print drink
print(drink.left.data) # should be print hot 
print(drink.left.left.data)   # should be print tea 
print(drink.left.right.data)   # should be print  coffee
print(drink.right.data)   # should be print cold
print(drink.right.left.data)   # should be print cola 
print(drink.right.right.data)   # should be print fanta 


