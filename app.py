from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

from api_handlers import (
    start_new_topic,
    submit_answer_to_ai,
    get_feedback,
    get_new_words,
)

app = Flask(__name__)
CORS(app)


@app.route("/new_topic", methods=["POST"])
@cross_origin()
def new_topic():
    language = request.json.get("language")
    new_topic = start_new_topic(language)

    new_words = get_new_words([], new_topic, language)
    response = make_response(
        {"status": "success", "new_topic": new_topic, "key_words": new_words}
    )

    return response


@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    conversation = request.json.get("conversation")
    language = request.json.get("language")
    response = submit_answer_to_ai(conversation, language)
    new_words = get_new_words(conversation, response, language)
    feedback = get_feedback(conversation, language)

    resp = {"ai_response": response, "feedback": feedback, "key_words": new_words}

    return jsonify({"status": "success", "results": resp})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
