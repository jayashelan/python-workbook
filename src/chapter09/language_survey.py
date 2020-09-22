from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn"
my_survey =AnonymousSurvey(question)

# show the qustion and store the responses
my_survey.show_question()

print('Enter q to quit \n')
while True:
	response =  input("Language::")
	if response =='q':
		break

	my_survey.store_responses(response)

# show the results
print("\n Thank You to everyone who participated in the survey")
my_survey.show_results()



