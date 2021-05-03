import socket 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  """
if __name__ == '__main__':
    app.run(host=socket.gethostname(),port=5000)