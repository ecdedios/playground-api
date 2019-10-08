from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return request.data
    else:
        return "Hello, stranger."

if __name__ == '__main__':
    import waitress
    waitress.serve(app, port=5005)
