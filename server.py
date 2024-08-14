''' This is a flask app that returns the emotions of the given input
    string
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion():
    ''' This function analyzes the input text and returns the
        emotions with the dominant emotion mentioned
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response["dominant_emotion"]
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response = ", ".join([f"'{key}': {value}" for key, value in response.items()])
    final_output = (
        f"For the given statement, the system's response is:\n"
        f"{response}.\n"
        f"The dominant emotion is '{dominant_emotion}'."
    )
    return final_output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
