from main import app
from flask import jsonify
import datetime

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    time = datetime.datetime.now().isoformat()
    health = "It`s works!"
    data = {
        "time": time,
        "health": health
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()