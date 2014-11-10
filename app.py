from flask import Flask
from flask import jsonify
from calc import is_prime

app = Flask(__name__)

@app.route("/<n>")
def calculate(n):
    # print 'n', n
    # print request.full_path
    result = {
        "n": n,
        "prime": is_prime(int(n))
    }

    return jsonify(**result)

if __name__ == '__main__':
    app.run(debug = True)
