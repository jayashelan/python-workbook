class AnonymousSurvey:
	"""Collect annonymous asnwers to the questions"""

	def __init__(self,question):
		"""Store the question and prepare the responses"""
		self.question  = question
		self.responses = []

	def show_question(self):
		"""show the survey question"""
		print(self.question)

	def store_responses(self,response):
		"""store the responses to the list"""
		self.responses.append(response)

	def show_results(self):
		"""show all  the responses"""
		print("Response Results")
		for response in self.responses:
			print(f" - {response} ")



			

