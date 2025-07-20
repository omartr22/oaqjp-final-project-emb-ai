from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        # Get the text statement from the form or JSON body
        text = request.form.get('text') or request.json.get('text')
        if not text:
            return "No text provided", 400

        result = emotion_detector(text)

        # Format the response string as requested
        response_str = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']}, "
            f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )
        return response_str

    # On GET, just render the HTML form (index.html)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
