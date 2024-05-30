from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    getreq= redis.get('hits')
    return 'Hello World! I have been seen {} so many times and the value is {}.\n'.format(count, getreq)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4200, debug=True)