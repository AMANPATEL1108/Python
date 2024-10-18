a=10
# b=20\

if a==18:
    # print("YPu can Vote")
    print("Ja ke Voter id Nikal")
elif a>18: 
    print("You can Vote")
    # print("False")
else:
    print("Bhagg")


firt=input("First NUmber:")
op=input("ENter a Operator")
sec=input("Second NUmber:")


firt=int(firt)
sec=int(sec)

if op=='+':
    print(firt+sec)
elif op=='-':
    print(fir-sec)
elif op=='*':
    print(firt*sec)
elif op=='/':
    print(firt/sec)
else:
    print("Eter a Valid Number")