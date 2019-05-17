from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>') 
def say(name):
    print(name)
    return "Hi, " + str(name) + '!'

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
  num = int(num)
  name = str(name)
  for i in range(0, num):
    print(name)
  return f"{name}<br/>" * num

if __name__ == '__main__':
    app.run(debug=True)
