d = 0
try:
    x = int(input("Введите целое число: "))
    stok = x
    x = abs(x)
    b = x
    while b>0 :
        a = x % 10
        b = x // 10
        d = d * 10 + a
        x = b
    if stok > 0:
        print(d)
    else:
        print (d * -1)
except ValueError as message :
    print ("Вы делаете что-то не то, попробуйте ввести целое число")
    

    


	    
       

	
