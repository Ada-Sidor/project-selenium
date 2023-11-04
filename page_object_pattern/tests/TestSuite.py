import unittest
from Test_Home_Page import HomePageTest
from Test_Step_two import StepTwoPageTest as StepTwoPageTest
from Test_Step_four import StepFourPageTest


""" Create the test suite"""
test_suite = unittest.TestSuite()

""" Adding test cases to the test suite """
test_suite.addTest(unittest.makeSuite(HomePageTest))
test_suite.addTest(unittest.makeSuite(StepTwoPageTest))
test_suite.addTest(unittest.makeSuite(StepFourPageTest))

""" Run the test suite """
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
