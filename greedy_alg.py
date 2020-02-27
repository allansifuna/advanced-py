class Food():
    """docstring for Food"""
    def __init__(self,value,calories,name):
        self.value = value
        self.calories=calories
        self.name=name

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calories

    def density(self):
        return self.get_value()/self.get_cost()

    def __str__(self):

        return f"{self.name}: <{self.get_value()},{self.get_cost()}>"

def build_menu(names,values,calories):
    """
        Takes a list of names, values and calories and returns a menu
    """
    menu=[]
    for i in range(len(names)):
        menu.append(Food(values[i],calories[i],names[i]))

    return menu

def greedy(items,max_cost,key_function):
    result=[]
    item_sorted=sorted(items,key=key_function,reverse=True)
    total_value,total_cost=0.0,0.0

    for i in range(len(item_sorted)):
        if total_cost + item_sorted[i].get_cost()<=max_cost:
            result.append(item_sorted[i])
            total_cost+=item_sorted[i].get_cost()
            total_value+=item_sorted[i].get_value()

    return (result,total_value)

def test_greedy(items,constraint,key_function):
    taken,val=greedy(items,constraint,key_function)
    print(f"The total value is {val}")

    for item in taken:
        print("   ",item)

def test_greedys(food,max_units):
    print(f'Use greedy by value to allocate {max_units} calories')
    test_greedy(food,max_units,Food.get_value)
    print(f'Use greedy by cost to allocate {max_units} calories')
    test_greedy(food,max_units,lambda x: 1/Food.get_cost(x))
    print(f'Use greedy by density to allocate {max_units} calories')
    test_greedy(food,max_units,Food.density)

names=['wine','beer','pizza','burger','fries','cola','apple','dougnut']
values=[89,90,95,100,90,79,50,10]
calories=[123,154,258,354,365,150,95,195]
food=build_menu(names,values,calories)
test_greedys(food,1000)
