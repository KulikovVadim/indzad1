d = 0
try:
	x = int(input("Введите целое число: "))
	b = x
	while b>0 :
	    a = x % 10
	    b = x // 10
	    d = d * 10 + a
	    x = b
	print(d)
except ValueError as message :
	print ("Вы делаете что-то не то, попробуйте ввести целое число")
    

    


	    
       

	
