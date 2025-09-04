import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Diccionario por defecto para casos de error o entrada vacía
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    # Manejo de entrada vacía
    if not text_to_analyze.strip():
        return empty_result

    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)

        # Manejo de status_code 400
        if response.status_code == 400:
            return empty_result

        response.raise_for_status()
        formatted_response = response.json()

        emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": emotion_scores.get("anger"),
            "disgust": emotion_scores.get("disgust"),
            "fear": emotion_scores.get("fear"),
            "joy": emotion_scores.get("joy"),
            "sadness": emotion_scores.get("sadness"),
            "dominant_emotion": dominant_emotion,
        }

    except requests.exceptions.RequestException as e:
        print(f"Error contacting the API: {e}")
        return empty_result
