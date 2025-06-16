#python version 3.12

#recursion algorithm 

def recursion(n):
	if n <= 1:
		return n 
	else:
		return recursion(n-1) * n # return n * recursion(n-1) will do too.

print(recursion(5)) # 5 is the nth number.

#test it open your terminal make sure python 3 is install and type in the console python recrusion.py