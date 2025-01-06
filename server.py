""" import flask and functiion dependencies"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detection():
    """
    Handles the '/emotionDetector' route, processes the text input,
    and returns the dominant emotion with other emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Text to analyze is missing. Please provide valid text."

    response = emotion_detector(text_to_analyze)

    if not response.get('dominant_emotion'):
        return "Invalid text! Please try again."

    # Format the response for the user
    return (f"For the given statement, the system response is: "
            f"anger: {response['anger']}, disgust: {response['disgust']}, "
            f"fear: {response['fear']}, joy: {response['joy']}, and "
            f"sadness: {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.
    """
    return render_template('index.html')

def run_app():
    """
    Starts the Flask application on port 5004.
    """
    app.run(host="0.0.0.0", port=5004)

if __name__ == "__main__":
    run_app()
