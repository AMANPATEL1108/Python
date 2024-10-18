def prime(a):  
    if a <= 1:  
        print("false")  
        return  

    for i in range(2, int(a ** 0.5) + 1):  
        if a % i == 0:  
            print("false")  
            return  
    print("true")  

prime(11)