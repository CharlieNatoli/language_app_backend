from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

from api_handlers import start_new_conversation, continue_conversation
import time

app = Flask(__name__)
CORS(app)

@app.route('/new_conversation', methods=['GET'])
@cross_origin()
def new_conversation_api():
    language= "Spanish"
    new_conversation = start_new_conversation(language)
    response = make_response({'status': 'success', 'new_conversation': new_conversation})


    return response


@app.route('/continue_conversation',  methods=['POST'])
def continue_conversation_api():
    conversation = request.json.get('conversation')
    print('REQUEST RECEIVED FOR CONTINUE CONVO')
    print("conversation", conversation)
    response = continue_conversation(conversation)
    print('DONE')
    resp = {
      "ai_response":response,
      "feedback": """
        Style:: could work on XYZ
        Word Choice:: the word \" blah\" does not work here
        Grammar:: you use of the Pluperfect subjunctive text is groovy here
      """ ,
      "key_words": "Agora: now. \n Nao: no. \n San Q: thanks babe"
    }

    # Handle POST request data here
    return jsonify({
      'status': 'success',
      'results': resp
    })


if __name__ == '__main__':
  app.run(debug=True, port=5000)

