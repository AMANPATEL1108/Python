weight=int(input("Weight"))
unit=input("(K)g or (L)bs:")
if unit.upper()=="K":
    converted=weight/0.45
    print("Weight in lbs:"+str(converted))
else:
    converted=weight=weight*0.45
    print("weight in kgs:"+str(converted))