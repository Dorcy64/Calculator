def new_calc():
	import art
	print(art.logo)
	#ADD
	def add(n1, n2):
		return n1 + n2

	#Subtract
	def subtract(n1, n2):
		return n1 - n2

	#Multiply
	def multiply(n1, n2):
		return n1 * n2

	# Divide
	def divide(n1, n2):
		return n1 / n2

	# Squared
	def squared(n1, n2):
		return n1 ** n2

	operations = {
		"/": divide,
		"+": add,
		"-": subtract,
		"*": multiply,
		"**": squared,
	}

	answer = float(input("What is the first number: "))

	def calculator(answer):

		for x in operations:
			print(x)

		operation_sumbol = str(input("Pick an operation from the operators above: "))
		num2 = float(input("What is the other number: "))

		function = operations[operation_sumbol]
		answer1 = function(answer, num2)

		print(f"{answer} {operation_sumbol} {num2} = {answer1}")
		return answer1

	break_num = 0
	break_num_do = 0
	while 1 > break_num:
		answer = calculator(answer)
		while 1 > break_num_do:
			do_continue = input("Do you want to contiue? y or n: ")
			if do_continue == "n":
				break_num += 1
				break_num_do += 1
				new_calc()
			elif do_continue == "y":
				break

new_calc()


