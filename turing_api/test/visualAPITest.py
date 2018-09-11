import unittest
import os
from turing_api.lib.visualAPI import VisualAPI

class VisualAPITest(unittest.TestCase):

	def test_a_autocrop(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.autocrop('https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		self.assertEqual([179, 163, 599, 1026], response["boxes"][0])
		self.assertEqual([329, 270, 683, 849], response["boxes"][1])
		self.assertEqual([1, 374, 160, 601], response["boxes"][2])

	def test_b_insert(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.insert('unit_test_id','https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		self.assertGreaterEqual(True, response["success"])

	def test_c_visualsearch(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.search('https://storage.googleapis.com/turingiq/unit_test_images/backpack-1.jpg')
		self.assertGreaterEqual(0.99, response['similar'][0]['similarity'])

	def test_d_recommendations(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.recommendations('unit_test_id')
		self.assertGreaterEqual(len(response["similar"]),1)

	def test_e_delete(self):
		visualAPI = VisualAPI(os.environ['API_KEY'],'sandbox')
		response = visualAPI.delete('unit_test_id')
		self.assertEqual(True, response["success"])


if __name__ == '__main__':
    unittest.main()
