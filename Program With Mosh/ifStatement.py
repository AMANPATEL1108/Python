# temp=3

# if temp>10:
#     print("More then 10")
# else:
#     print("Less then 10")



firt=input("First NUmber:")
op=input("ENter a Operator")
sec=input("Second NUmber:")


firt=int(firt)
sec=int(sec)

if op=='+':
    print(firt+sec)
elif op=='-':
    print(firt-sec)
elif op=='*':
    print(firt*sec)
elif op=='/':
    print(firt/sec)
else:
    print("Eter a Valid Number")