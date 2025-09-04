# Emotion Detection AI Application

## 📚 Project Overview

This is a **Final Project** for the **"Developing AI Applications with Python and Flask"** course offered by **Coursera**. The application demonstrates the integration of AI-powered emotion detection capabilities with a modern web interface built using Python Flask.

## 🎯 What It Does

The Emotion Detection AI Application analyzes text input and identifies the emotional content, providing scores for five primary emotions:
- **Anger** 😠
- **Disgust** 🤢  
- **Fear** 😨
- **Joy** 😊
- **Sadness** 😢

The system determines the **dominant emotion** based on the highest confidence score and presents results in an easy-to-understand format.

## 🏗️ Architecture

- **Backend**: Python Flask web server
- **AI Service**: IBM Watson NLP Emotion Detection API
- **Frontend**: HTML5 + Bootstrap + Vanilla JavaScript
- **API Integration**: RESTful API calls to Watson services

## 🚀 Features

- Real-time emotion analysis
- RESTful API endpoint (`/emotionDetector`)
- Modern, responsive web interface
- Comprehensive error handling
- Unit test coverage
- Clean, modular code structure

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (for Watson API access)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd oaqjp-final-project-emb-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python server.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 Usage

### Web Interface
1. Open the application in your browser
2. Enter the text you want to analyze in the input field
3. Click "Run Sentiment Analysis"
4. View the emotion detection results

### API Usage
You can also use the API directly:

```bash
GET /emotionDetector?textToAnalyze=your_text_here
```

**Example Response:**
```json
{
  "anger": 0.1,
  "disgust": 0.05,
  "fear": 0.02,
  "joy": 0.8,
  "sadness": 0.03,
  "dominant_emotion": "joy"
}
```

## 🧪 Testing

Run the test suite to verify everything works correctly:

```bash
python test_emotion_detection.py
```

The tests cover various emotion scenarios including joy, anger, disgust, sadness, and fear.

## 🏗️ Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/           # Core emotion detection module
│   ├── __init__.py
│   └── emotion_detection.py   # Main emotion analysis logic
├── static/                     # Static assets
│   └── mywebscript.js         # Frontend JavaScript
├── templates/                  # HTML templates
│   └── index.html             # Main web interface
├── server.py                   # Flask application server
├── test_emotion_detection.py  # Unit tests
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## 🔧 Configuration

The application uses the IBM Watson NLP Emotion Detection API. The API endpoint and model configuration are set in `EmotionDetection/emotion_detection.py`.

## 🚨 Error Handling

The application gracefully handles various error scenarios:
- Empty or invalid text input
- API service unavailability
- Network connection issues
- Invalid API responses

## 🤝 Contributing

This is a course project, but suggestions and improvements are welcome. Please ensure any changes maintain the project's educational value and functionality.

## 📝 License

This project is created for educational purposes as part of the Coursera course "Developing AI Applications with Python and Flask".

## 👨‍🎓 Course Information

- **Course**: Developing AI Applications with Python and Flask
- **Platform**: Coursera
- **Institution**: IBM
- **Project Type**: Final Project - Emotion Detection AI Application

## 🆘 Troubleshooting

### Common Issues

1. **API Connection Errors**: Ensure you have internet access and the Watson API is available
2. **Module Import Errors**: Verify all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in `server.py` or stop other services using port 5000

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify your Python version (`python --version`)
3. Ensure all dependencies are properly installed
4. Check your internet connection

---

**Happy Emotion Detection! 🎉**

*Built with ❤️ for AI and Flask learning*
