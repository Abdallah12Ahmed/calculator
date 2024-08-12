def add(x,y):
	return x+y

def subtract(x,y):
	return x-y
	
def multiply(x,y):
	return x*y
	
def divide(x,y):
	return x/y
	
def calculator():
	print("select the operation: \n1- add\n2- subtract\n3- multiply\n4- divide\n")
	choice=input("enter the number or operation: ")
	num1=int(input("enter the first number: "))
	num2=int(input("enter the second number: "))
	
	if choice == '1':
		print("result = ",add(num1,num2))
		
	elif choice == '2':
		print("result = ",subtract(num1,num2))
		
	elif choice == '3':
		print("result = ",multiply(num1,num2))
		
	elif choice == '4':
		print("result = ",divide(num1,num2))
		
	else:
		print("invalid choice")
		
if __name__ =="__main__":
	calculator()
