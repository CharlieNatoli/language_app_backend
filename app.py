from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
print('server servinggg')


sample_data =  [ {
    'id': 1,
    'type': 'ai',
    'content': "Hola. Dime mas sobre tus comidas favoritas? Que te gusta mas y porque? "
  },
  {
    'id': 2,
    'type': 'user',
    'content': "I'd be happy to help you understand how to implement a classification model. Let's break this down into manageable steps and explore the key concepts you'll need to know."
  },
  {
    'id': 3,
    'type': 'ai',
    'content': "Let's break this down into manageable steps and explore the key concepts you'll need to know."

  },
  {
    'id': 4,
    'type': 'user',
    'content': "I'd be happy to help you understand how to implement a classification model. "
  },
  {
    'id': 5,
    'type': 'ai',
    'content': "I'd be happy to help you understand how to implement a classification model. Let's break this down into manageable steps and explore the key concepts you'll need to know."
  },
  {
    'id': 6,
    'type': 'user',
    'content': "I'd be happy to help you understand how to implement a classification model. "
  }
  ]

@app.route('/new_conversation',  methods=['GET', 'POST'])
def new_conversation():
  print('REQUEST RECEIVED - SLEEPING')
  time.sleep(1)
  print('DONE')
  # Handle POST request data here
  return jsonify({'status': 'success', 'convo': sample_data})


@app.route('/add_response',  methods=['GET', 'POST'])
def add_response():
  print('REQUEST RECEIVED')
  # Handle POST request data here
  return jsonify({'status': 'success', 'convo': sample_data})


if __name__ == '__main__':
  app.run(debug=True, port=5000)

