import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=data)
    
    # If bad input, return dictionary with None values
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    response_text = response.text
    response_dict = json.loads(response_text)
    emotions = response_dict['predictions'][0]['classes']

    scores = {emotion['class']: emotion['score'] for emotion in emotions}
    dominant = max(scores, key=scores.get)
    
    return {
        'anger': scores.get('anger'),
        'disgust': scores.get('disgust'),
        'fear': scores.get('fear'),
        'joy': scores.get('joy'),
        'sadness': scores.get('sadness'),
        'dominant_emotion': dominant
    }

