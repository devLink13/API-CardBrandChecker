from flask import Flask, render_template
from routes.info_card import bp_info_card

app = Flask(__name__)

app.register_blueprint(bp_info_card)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
