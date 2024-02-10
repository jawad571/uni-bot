from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    data = request.get_json()

    if 'message' in data:
        message = data['message']
        response = {
            'status': 'success',
            'message': f'You said: {message}'
        }
    else:
        response = {
            'status': 'error',
            'message': 'No message provided'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
