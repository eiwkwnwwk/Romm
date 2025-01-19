from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    start_time = request.args.get('start_time', time.time())  # Retrieve or set start time
    load_time = time.time() - float(start_time)  # Calculate elapsed time
    return f"<h1>You took {load_time:.2f} seconds to visit this website.</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
