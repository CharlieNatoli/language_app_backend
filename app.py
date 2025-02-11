from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

from api_handlers import start_new_conversation, continue_conversation, get_feedback, get_new_words
import time

app = Flask(__name__)
CORS(app)

@app.route('/new_conversation', methods=['GET'])
@cross_origin()
def new_conversation_api():
    language= "Spanish"
    new_conversation = start_new_conversation(language)

    new_words = get_new_words([], new_conversation)
    response = make_response({
        'status': 'success',
        'new_conversation': new_conversation,
        'key_words': new_words

    })

    return response


@app.route('/continue_conversation',  methods=['POST'])
def continue_conversation_api():
    conversation = request.json.get('conversation')
    print('REQUEST RECEIVED FOR CONTINUE CONVO')
    print("conversation", conversation)
    response = continue_conversation(conversation)
    new_words = get_new_words(conversation, response)
    feedback = get_feedback(conversation)
    print('DONE')

    resp = {
      "ai_response":response,
      "feedback": feedback,
      "key_words": new_words
    }

    # Handle POST request data here
    return jsonify({
      'status': 'success',
      'results': resp
    })


if __name__ == '__main__':
  app.run(debug=True, port=5000)

