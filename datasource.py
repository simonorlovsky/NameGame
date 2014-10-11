#Hami Abdi, Simon Orlovsky, & Caleb Braun

''' a class that retrieves a fun fact based on your given information
and specified question '''
class DataSource:
	'''lastName will be a string, ethnicity will be a string, and question
	will be in terms of a number -- for instance, question number 0. There
	are a maximum of 5 question, and an "all questions" default.'''
	def __init__(self, lastName, ethnicity, question):
		this.lastName = lastName
		this.ethnicity = ethnicity
		this.question = question

	def getAnswer():
		'''a helper function that will call/implement the correct
		function to retreive the fun fact corresponding to the given
		question. The 'result' will be a list containing the calculated result(s)'''
		result = []
		if this.question == 0:
			result += this.resultOfQuestion1()
		if this.question == 1:
			result += this.resultOfQuestion2()
		if this.question == 2:
			result += this.resultOfQuestion3()
		if this.question == 3:
			result += this.resultOfQuestion4()
		if this.question == 4:
			result += this.resultOfQuestion5()
		else:
			result +=this.resultOfAllDefault()
		return result
	
	def resultOfQuestion1():
		'''will retrieve corresponding data to return a list
		containing a string that provides an answer to Question 1 '''
		return ['s']

	def resultOfQuestion2():
		'''will retrieve corresponding data to return a list
		containing a string that provides an answer to Question 2 '''
		return ['s']
	def resultOfQuestion3():
		'''will retrieve corresponding data to return a list
		containing a string that provides an answer to Question 3 '''
		return ['s']
	def resultOfQuestion4():
		'''will retrieve corresponding data to return a list
		containing a string that provides an answer to Question 4 '''
		return ['s']
	def resultOfQuestion5():
		'''will retrieve corresponding data to return a list
		containing a string that provides an answer to Question 5 '''
		return ['s']
	def resultOfAllDefault():
		'''will return a list containing as many strings as there are
		questions to ask, containing the corresponding answer to all of
		them '''
		return ['s', 's', 's', 's', 's']








