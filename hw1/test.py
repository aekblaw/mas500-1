#Unit test file for Forked repo script from JasRub
#code adapted from RahulBot (instructor)

import unittest
import hw1


class hw1APItest(unittest.TestCase):

	def testApiCall(self):
		result =  hw1.apiCall() 
		assert result[0] != None
		assert result[1] != None

if __name__ == "__main__":
    unittest.main()

