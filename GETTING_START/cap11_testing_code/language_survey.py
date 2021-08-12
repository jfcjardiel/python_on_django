##using unittest to test a class
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        ##testing if the class strores the languages
        for response in responses:
            my_survey.store_response(response)
        #test if each one of the langues are in te class instance
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main() 