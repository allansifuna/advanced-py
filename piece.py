import itertools
class Pieces():
    """docstring for Pieces"""
    def __init__(self, num,val):
        self.num = num
        self.val=val

    def getVal(self):
        return self.val

    def getNum(self):
        return self.num

    def __str__(self):
        return f"{self.num}:<{self.val}>"
    def __repr__(self):
        return f"{self.num}:<{self.val}>"


def buildModel(nums,vals):
    result=[]

    for i in range(len(nums)):
        result.append(Pieces(nums[i],vals[i]))

    return result



def maxVal(pieces,length):
    if pieces == [] or length==0:
        result=(0,())
    else:
        nextItem=pieces[0]
        optval,vals=maxVal(pieces[0:],length-nextItem.getNum())
        optval+=nextItem.getVal()


        woptval,wvals=maxVal(pieces[0:],length)
        if woptval>optval:
            result=(woptval,wvals+(nextItem,))
        else:
            result=(optval,vals+(nextItem,))

    return result

def all(pieces,length):
    optval=[]
    allcombs=[]

    for i in pieces:
        le=0
        comb=[]
        for j in pieces:
            if le +j.getNum()<length:
                comb.append(j)
        allcombs.append(comb)

    for comb in allcombs:
        combval=0
        for co in comb:
            combval+=co.getVal()
        optval.append(combval)


    a=max(optval)
    v=optval.index(a)
    return (a,allcombs[v])

def getPermutations(f):
    yield from list(itertools.permutations(f,len(f)))



nums=[1,2,3,4]
r=len(nums)
vals=[1,5,8,9]
length=8
pieces=buildModel(sorted(nums,reverse=True),sorted(vals,reverse=True))
# optval,vals=all(pieces,length)

def get_perms(pieces):
    complete_list=[]
    for current in range(r+1):
        a=[i for i in pieces]
        for y in range(current):

            a=[[x]+[i] for x in pieces for i in a]
        complete_list+=a
    yield complete_list

a=get_perms(pieces)

# for s in iter(a):
#     print(s)

def use(l):

    if type(l) is not list:
        return l
    elif  type(l[1]) is not list:
        return l
    try:
        lis=[]
        lis=use(l[1])
        lis.append(l[0])
    except IndexError:
        return [l[0]]
    return lis

weights=0
toConsider = []
for i in iter(a):
    for c in i:
        v=[use(c)]
        for i in v :
            leng=0
            if type(i) is not list:
                leng=i.getNum()
                if leng>weights:
                    weights=leng
                    toConsider=[i]
            else:
                for j in i:
                    leng+=j.getNum()
                if leng>weights and leng<=length:
                    weights=leng
                    toConsider=i
print(toConsider)
print(weights)

# optval=0
# combi=[]
# for b in iter(a):
#     print(b)
#     totalval=0
#     c=list(b)
#     for i in c:
#         totalval+=i.getVal()

#     if totalval>optval:
#         optval=totalval
#         combi=c

# print(optval)
# print(combi)
