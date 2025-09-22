import requests

def emotion_detector(text_to_analyse):
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }
    # Custom header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=input_json, headers=header)
    # Returning the text attribute of the response object
    return response.text
    