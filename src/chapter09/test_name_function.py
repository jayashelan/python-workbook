import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Test for 'name_function.py'"""

	def test_first_name(self) :
		"""Do names like Janis Joplin work ? """
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like Wolfgang Amadues Mozart's work ?"""
		formatted_name = get_formatted_name('Wolfgang','mozart','amadues')
		self.assertEqual(formatted_name,'Wolfgang Amadues Mozart')



if __name__ == '__main__':
	unittest.main()







