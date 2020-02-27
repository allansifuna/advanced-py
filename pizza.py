import os
class Pizza():
    def __init__(self,name,size):
        self.name=name
        self.size=size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}:<{self.size}>"
    def __repr__(self):
        return f"{self.name}:<{self.size}>"


def build_order(names,sizes):
    order=[]
    for i in range(len(sizes)):
        order.append(Pizza(names[i],sizes[i]))
    return order

def greedy(items,max_people,key_function):
    total_size=0
    result=[]
    sizes=[]
    items_copy=sorted(items,key=key_function,reverse=True)

    for i in range(len(items_copy)):
        if total_size+items_copy[i].get_size()<=max_people:
            if items_copy[i].get_size() not in sizes:
                sizes.append(items_copy[i].get_size())
                total_size+=items_copy[i].get_size()
                result.append(items_copy[i])
    return (result,total_size)
def parse_from_file(file):

    max_people,pizza_types=0,0
    sizes=[]
    with open(file,'r') as f:
        max_people,pizza_types=f.readline().split(" ")
        sizes=f.readline().split(" ")
        _sizes=[int(i) for i in sizes]
    return (int(max_people),pizza_types,_sizes)

def test_greedy(file):
    print("Testing greedy")
    max_people,pizza_types,sizes=parse_from_file(file)
    names=[i for i in range(0,int(pizza_types))]
    output((file,greedy(build_order(names,sizes),max_people,Pizza.get_size)))
    return True



def output(tupl):
    folder='out/'
    file,tup=tupl
    res,tot=tup
    file=folder+file
    with open(file,'w') as f:
        f.write(str(len(res))+"\n")
        to_write=[ int(i.get_name()) for i in res]
        to_write= sorted(to_write)
        new_to_write=[str(i) for i in to_write]
        f.write(" ".join(new_to_write))

files=['a_example.in','b_small.in','c_medium.in','d_quite_big.in','e_also_big.in']

for file in files:
    test_greedy(file)

