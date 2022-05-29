from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
  

@app.route('/stocks', methods=['GET', 'POST'])
def stocks():
  url = ('https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.csv')
  response = request.get(url)
  response.json()



if __name__ == "__main__":
  app.run()
  