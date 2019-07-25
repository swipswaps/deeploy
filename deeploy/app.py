from bottle import Bottle, run

app = Bottle()

@app.route( '/' )
def home():
  return 'Deeploy.';

@app.post('/')
def main():
  return 'Here goes'


run(app, host='localhost', port=8123)
