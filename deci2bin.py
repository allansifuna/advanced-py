def convert(number):
    num= number
    binary=[]
    counter=0
    checker=True

    while (checker):
        temp_num=num*2
        if temp_num>1:
            binary.append('1')
            num=temp_num-1
        elif temp_num==1:
            binary.append('1')
            checker=False
        elif temp_num<1:
            binary.append('0')
            num=temp_num
        counter+=1
        if counter==10000:
            checker=False

    return binary


a=convert(0.3)
print(f"0.{''.join(a)}")
