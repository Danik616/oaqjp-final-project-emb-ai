"""
Flask application for emotion detection
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_flask():
    """
    Flask route to detect emotions from a given statement.

    Returns:
        JSON response containing the emotion analysis or error message.
    """
    try:
        statement = request.args.get('textToAnalyze')
        if not statement:
            return jsonify({"error": "Invalid text! Please try again!"}), 400
        emotions = emotion_detector(statement)

        if emotions['dominant_emotion'] is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400
        dominant_emotion = emotions['dominant_emotion']
        response = (
            f"For the given statement, the system response is 'anger': {emotions['anger']}, "
                    f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
                    f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
                    f"The dominant emotion is {dominant_emotion}.")
        return jsonify({"response": response}), 200
    except KeyError as err:
        return jsonify({"error": f"Key error: {err}"}), 400
    except ValueError as err:
        return jsonify({"error": f"Value error: {err}"}), 400

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)