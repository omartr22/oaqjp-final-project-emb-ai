"""
server.py

Flask web server for the Emotion Detection application.
Handles HTTP requests and returns emotion analysis results.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handles emotion detection for user-submitted text.
    POST: Accepts a text input and returns emotion analysis.
    GET: Renders the homepage with a form.
    """
    if request.method == 'POST':
        text = request.form.get('text') or (request.json and request.json.get('text'))

        if not text:
            return "Invalid text! Please try again!", 400

        result = emotion_detector(text)

        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!", 400

        response_str = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']}, "
            f"and 'sadness': {result['sadness']}. The dominant emotion is "
            f"{result['dominant_emotion']}."
        )
        return response_str

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
