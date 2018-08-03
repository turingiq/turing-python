import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib import VisualAPI

class VisualAPITest(unittest.TestCase):

	def testAutoCrop(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.autocrop('https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		self.assertEqual([188, 256, 656, 928], response["boxes"][0])
		self.assertEqual([379, 343, 651, 870], response["boxes"][1])

	def testVisualSearch(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.search('https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		# self.assertGreaterEqual(0.99, response['similar'][0]['similarity'])

	def testInsert(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.insert('unit_test_id','https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		self.assertGreaterEqual(True, response["success"])

	def testVisualRecommendations(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.recommendations('unit_test_id')
		self.assertGreaterEqual(len(response["similar"]),1)

	def testDelete(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.delete('unit_test_id')
		# print(response)
		self.assertEqual(True, response["success"])


if __name__ == '__main__':
    unittest.main()