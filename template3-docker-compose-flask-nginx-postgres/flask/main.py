from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Why Hello World ? XD'

# if __name__ == '__main__':
#     app.debug = True
#     app.run()