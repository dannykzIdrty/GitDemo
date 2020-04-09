print ("It is an calculator , calculate variable a and variable b")
print ("Input the function and calculate with two variables followed by instruction")

while True: 
	try:
		
		a = input("\ninput a=")
		
		f = input("\nFunction list:" +
		"\naddition input:+" +
		"\nsubtraction input: -"+
		"\nmultiplication input: x or *"+
		"\ndivision for / or ÷"+
		"\nindex input: ** or xx"+
		"\nsquare root input: sqrt"+
		"\n\nPlease input"+
		"\n\ninput function=")
		if f =="sqrt":
			print ("only the result of square root of a will be printed out")
		
		b = input("\ninput b=")
		if f == "+":
			answer = int(a) + int(b)
			print ("\naddition=" +str(answer))
		elif f == "x" or f == "*":
			answer = int(a) * int(b)
			print ("\nmultiplication=" + str(answer))
		elif f == "÷" or f == "/":
			answer = int(a) / int(b)
			print ("\ndivision=" + str(answer))
		elif f == "-":
			answer = int(a) - int(b)
			print ("\nsubtraction=" + str(answer))
		elif f == "**" or f == "xx":
			answer = int(a) ** int(b)
			print ("\nanswer=" + str(answer))
		elif f == "sqrt":
			import math
			answer = math.sqrt(int(a))
			print ("\nsquare root of a=" + str(answer))
		
		if f != "sqrt":
			print ("\nsolution=\n"+ a + f + b + "=" + 							str(answer))
		print ("\nfinished calculation")
		print ("\n\n\nanother calculation")
		
		continue
		
	except :
		print ("\nEither/both a or b is/are not (an) integer(s) or incorrect function")
		print ("\nPlease restart the programme \nCheck your input to make sure you follow the instruction carefully")
		break