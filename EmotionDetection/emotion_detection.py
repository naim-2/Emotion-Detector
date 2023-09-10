"""
Emotion Detection File
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """Function to call emotion detector from the Watson URL"""
    url = """https://sn-watson-emotion.labs.skills.network/v1/
    watson.runtime.nlp.v1/NlpService/EmotionPredict"""
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=2.5)
    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger = formatted_response['documentEmotion']['anger']
        disgust = formatted_response['documentEmotion']['disgust']
        fear = formatted_response['documentEmotion']['fear']
        joy = formatted_response['documentEmotion']['joy']
        sadness = formatted_response['documentEmotion']['sadness']
        dominant_emotion = max(anger, disgust, fear, joy, sadness)
        
    dictionary = {'anger': anger, 'disgust': disgust, 'fear': fear, 
    'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    
    return dictionary
    
