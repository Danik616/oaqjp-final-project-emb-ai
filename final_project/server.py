from Flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text = str(request.args.get('text'))
    result = emotion_detector()
