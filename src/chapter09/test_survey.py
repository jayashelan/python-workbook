import unittest
from survey import AnonymousSurvey 

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""

	def setUp(self):
		"""Creat a survey and a set of responses for use in all test methods"""
		question = "What language did you first learn to speak ?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Spanish','French']

	def test_store_single_response(self):
		"""Test that a single response is stored properly"""
		self.my_survey.store_responses('English')
		self.assertIn('English',self.my_survey.responses)

	def test_three_store_responses(self):
		"""Test for three responses"""
		
		for response in self.responses:
			self.my_survey.store_responses(response)

		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)

		

if __name__ == '__main__':
	unittest.main()


