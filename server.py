"""
Emotion Detection AI Application - Flask Server

This module contains a Flask web application for detecting emotions in text using
IBM Watson NLP services. The application provides both a web interface and a RESTful
API endpoint for emotion analysis.

Author: Sabnei
Course: Developing AI Applications with Python and Flask (Coursera)
Institution: IBM
Project Type: Final Project

Features:
    - Web interface for text input and emotion analysis
    - RESTful API endpoint for programmatic access
    - Integration with IBM Watson Emotion Detection API
    - Error handling and validation
    - Real-time emotion scoring for 5 primary emotions

Dependencies:
    - Flask: Web framework
    - EmotionDetection.emotion_detector: Core emotion analysis module

Usage:
    python server.py
    
    Then open http://localhost:5000 in your browser
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application with a descriptive name
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    RESTful API endpoint for emotion analysis.
    
    This endpoint analyzes the emotional content of provided text using the
    IBM Watson NLP Emotion Detection API. It returns a formatted response
    with emotion scores and the dominant emotion.
    
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotional content.
                            Must be a non-empty string.
    
    Returns:
        str: A human-readable formatted string with emotion analysis results.
             Format: "For the given statement, the system response is 'anger': X,
                     'disgust': Y, 'fear': Z, 'joy': A and 'sadness': B.
                     The dominant emotion is {dominant_emotion}."
    
    Error Responses:
        - "Invalid text! Please try again!" if text is empty, None, or invalid
        
    Example:
        GET /emotionDetector?textToAnalyze=I am very happy today
        
    Note:
        This endpoint is designed for educational purposes and demonstrates
        integration with AI services for emotion detection.
    """
    
    # Extract text parameter from the request query string
    text_to_analyze = request.args.get("textToAnalyze")
    
    # Call the emotion detection service to analyze the text
    response = emotion_detector(text_to_analyze)

    # Format the response in a human-readable format
    # This creates a natural language description of the emotion analysis results
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    # Check if the analysis was successful (dominant_emotion is not None)
    if response["dominant_emotion"] is not None:
        return formatted_response
    
    # Return error message if the analysis failed
    return "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    """
    Serves the main web interface for the Emotion Detection application.
    
    This endpoint renders the index.html template, which provides a user-friendly
    web interface for entering text and viewing emotion analysis results.
    
    Returns:
        str: Rendered HTML content of the main application page.
        
    Template:
        templates/index.html: Contains the web form and JavaScript for
                             user interaction and API calls.
    
    Features:
        - Text input field for user text entry
        - Button to trigger emotion analysis
        - Results display area
        - Bootstrap styling for modern appearance
    """
    return render_template("index.html")


if __name__ == "__main__":
    """
    Application entry point.
    
    Starts the Flask development server with debug mode enabled.
    In production, consider using a WSGI server like Gunicorn.
    """
    # Start the Flask development server
    # debug=True enables auto-reload and detailed error messages
    app.run(debug=True)
