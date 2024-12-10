import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status() 
        response_data = response.json()

        emotion_data = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})

        anger = emotion_data.get('anger', 0)
        disgust = emotion_data.get('disgust', 0)
        fear = emotion_data.get('fear', 0)
        joy = emotion_data.get('joy', 0)
        sadness = emotion_data.get('sadness', 0)
            
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {str(e)}")
        return f"An error occurred: {str(e)}"
    except json.JSONDecodeError as json_error:
            print("Error al parsear la respuesta JSON:", json_error)
            return {"error": "Error al parsear la respuesta JSON del servicio."}
