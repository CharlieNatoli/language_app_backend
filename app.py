from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
print('server servinggg')


sample_data =  [ {
    'type': 'ai',
    'content': "Hola. Dime mas sobre tus comidas favoritas? Que te gusta mas y porque? "
  }
  ]

@app.route('/new_conversation',  methods=['GET', 'POST'])
def new_conversation():
  print('REQUEST RECEIVED - SLEEPING')
  time.sleep(1)
  print('DONE')
  # Handle POST request data here
  return jsonify({'status': 'success', 'new_conversation': sample_data})


@app.route('/add_response',  methods=['GET', 'POST'])
def add_response():
  print('REQUEST RECEIVED FOR ADD RESPONSE')
  time.sleep(1)
  print('DONE')
  resp = {
      "ai_response":"Verdaaaaad??? Dime masssss!!!",
      "feedback": "like TBH ur response is like so horrible lol",
      "key_words": "Agora: now. \n Nao: no. \n San Q: thanks babe"
  }

  # Handle POST request data here
  return jsonify({
      'status': 'success',
      'results': resp
  })


if __name__ == '__main__':
  app.run(debug=True, port=5000)

