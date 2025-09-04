"""
Emotion Detection Module

This module provides emotion detection functionality by integrating with the
IBM Watson NLP Emotion Detection API. It analyzes text input and returns
emotion scores for five primary emotions along with the dominant emotion.

Author: Sabnei
Course: Developing AI Applications with Python and Flask (Coursera)
Institution: IBM
Project Type: Final Project

Features:
    - Text-based emotion analysis
    - Support for 5 primary emotions: anger, disgust, fear, joy, sadness
    - Automatic dominant emotion detection
    - Error handling and fallback responses
    - Input validation

Dependencies:
    - requests: HTTP library for API calls

API Endpoint:
    IBM Watson NLP Emotion Detection Service
    URL: https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict
    Model: emotion_aggregated-workflow_lang_en_stock

Usage:
    from EmotionDetection.emotion_detection import emotion_detector
    
    result = emotion_detector("I am very happy today!")
    print(f"Dominant emotion: {result['dominant_emotion']}")
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotional content of the provided text.
    
    This function sends the input text to the IBM Watson NLP Emotion Detection
    API and returns a structured response with emotion scores and the dominant
    emotion. It includes error handling and input validation.
    
    Args:
        text_to_analyze (str): The text string to analyze for emotional content.
                              Should be a non-empty string with meaningful content.
    
    Returns:
        dict: A dictionary containing:
            - anger (float): Anger emotion score (0.0 to 1.0)
            - disgust (float): Disgust emotion score (0.0 to 1.0)
            - fear (float): Fear emotion score (0.0 to 1.0)
            - joy (float): Joy emotion score (0.0 to 1.0)
            - sadness (float): Sadness emotion score (0.0 to 1.0)
            - dominant_emotion (str): The emotion with the highest score
            
            Returns empty_result if analysis fails.
    
    Example:
        >>> result = emotion_detector("I am so excited about this project!")
        >>> print(result['dominant_emotion'])
        'joy'
        >>> print(result['joy'])
        0.85
    
    Notes:
        - Empty or whitespace-only text returns empty_result
        - API failures return empty_result
        - Emotion scores are normalized between 0.0 and 1.0
        - The dominant emotion is determined by the highest score
    """
    
    # IBM Watson NLP Emotion Detection API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers required for the API call
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Default response structure for error cases or empty input
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    # Input validation: check if text is empty or only whitespace
    if not text_to_analyze.strip():
        return empty_result

    # Prepare the request payload in the format expected by Watson API
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Make POST request to Watson Emotion Detection API
        response = requests.post(url, headers=headers, json=input_json)

        # Handle bad request errors (400 status code)
        if response.status_code == 400:
            return empty_result

        # Raise exception for other HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response from the API
        formatted_response = response.json()

        # Extract emotion scores from the API response
        # The API returns predictions in an array, we take the first one
        emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
        
        # Determine the dominant emotion by finding the emotion with highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return structured response with all emotion scores and dominant emotion
        return {
            "anger": emotion_scores.get("anger"),
            "disgust": emotion_scores.get("disgust"),
            "fear": emotion_scores.get("fear"),
            "joy": emotion_scores.get("joy"),
            "sadness": emotion_scores.get("sadness"),
            "dominant_emotion": dominant_emotion,
        }

    except requests.exceptions.RequestException as e:
        # Log any network or API-related errors
        print(f"Error contacting the API: {e}")
        return empty_result
