"""
Test Suite for Emotion Detection Module

This module contains unit tests for the emotion_detector function from the
EmotionDetection module. It tests various emotion scenarios to ensure
the emotion detection functionality works correctly.

Author: Sabnei
Course: Developing AI Applications with Python and Flask (Coursera)
Institution: IBM
Project Type: Final Project

Test Coverage:
    - Joy emotion detection
    - Anger emotion detection
    - Disgust emotion detection
    - Sadness emotion detection
    - Fear emotion detection

Dependencies:
    - unittest: Python's built-in testing framework
    - EmotionDetection.emotion_detector: The function being tested

Usage:
    python test_emotion_detection.py
    
    Or run with more verbose output:
    python -m unittest test_emotion_detection.py -v
"""

from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    """
    Test case class for emotion detection functionality.
    
    This class contains all the unit tests for the emotion_detector function.
    Each test method validates a specific emotion detection scenario.
    """
    
    def test_emotion_detection(self):
        """
        Test emotion detection for various emotional expressions.
        
        This test method validates that the emotion_detector function
        correctly identifies the dominant emotion in different types of text.
        It tests all five supported emotions: joy, anger, disgust, sadness, and fear.
        
        Test Cases:
            1. Joy: "I am glad this happened"
            2. Anger: "I am really mad about this"
            3. Disgust: "I feel disgusted just hearing about this"
            4. Sadness: "I am so sad about this"
            5. Fear: "I am really afraid that this will happen"
        
        Assertions:
            - Each test case should return the expected dominant emotion
            - The dominant_emotion key should be present in the response
            - The response should be a valid dictionary structure
        """
        
        # Test Case 1: Joy emotion
        # This text should be classified as expressing joy/happiness
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"], "joy")

        # Test Case 2: Anger emotion
        # This text should be classified as expressing anger/frustration
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2["dominant_emotion"], "anger")

        # Test Case 3: Disgust emotion
        # This text should be classified as expressing disgust/repulsion
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3["dominant_emotion"], "disgust")

        # Test Case 4: Sadness emotion
        # This text should be classified as expressing sadness/grief
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4["dominant_emotion"], "sadness")

        # Test Case 5: Fear emotion
        # This text should be classified as expressing fear/anxiety
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"], "fear")


# Main execution block for running tests
if __name__ == "__main__":
    """
    Test execution entry point.
    
    When this file is run directly, it will execute all the unit tests
    defined in the TestEmotionDetector class. This provides a simple way
    to run the test suite and verify the emotion detection functionality.
    
    Test Output:
        - Shows test results and any failures
        - Indicates the number of tests run and passed/failed
        - Provides detailed error information for failed tests
    """
    
    # Run all tests in the test suite
    # This will execute all test methods in the TestEmotionDetector class
    unittest.main()
