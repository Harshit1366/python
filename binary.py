a=int(input("Enter no :"))
list=[]

for i in range(8):
    b = a % 2
    a = (int)(a / 2)
    # print("b",b)
    # print("a",a)

    if b == 0:
        list.append(0)
    elif b==1:
        list.append(1)
    # elif b>=2 :
    #     list.append(1)
    # else:
    #     list.append(0)

list.reverse()
print(*list, sep='')