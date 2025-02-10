from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

from api_handlers import start_new_conversation
import time

app = Flask(__name__)
CORS(app)

@app.route('/new_conversation', methods=['GET'])
@cross_origin()
def new_conversation():
    # language = request.args.get('language')
    language= "Spanish"
    print('REQUEST RECEIVED - SLEEPING')
    new_conversation = start_new_conversation(language)
    # new_conversation = "BLABA"
    print('DONE')
    print(new_conversation)
    response = make_response({'status': 'success', 'new_conversation': new_conversation})

    # Explicitly add CORS headers
    # response.headers.add('Access-Control-Allow-Origin', '*')  # Or your specific origin
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    # response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')

    return response


@app.route('/add_response',  methods=['GET', 'POST'])
def add_response():
  print('REQUEST RECEIVED FOR ADD RESPONSE')
  time.sleep(1)
  print('DONE')
  resp = {
      "ai_response":"Verdaaaaad??? Dime masssss!!!",
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

