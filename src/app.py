from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def neural_network():
    user_text = request.args.get('msg')
    return str(user_text)



if __name__ == '__main__':
    app.run(debug=True)
