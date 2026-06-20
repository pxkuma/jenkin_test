def add(int a, int b):
	return a+b
def divide(int a, int b):
	if b==0:
		raise ValueError("Cannot divide by zero")
	else:
		return a/b
