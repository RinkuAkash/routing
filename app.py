from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<uname>', methods=['GET'])
def index(uname):
    return jsonify({'User':uname})

if __name__ == '__main__':
    app.run(debug=True)