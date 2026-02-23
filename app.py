from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("lr_classifier.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "POST":
        try:
            time = float(request.form["time"])
            amount = float(request.form["amount"])
            pca_values = [float(request.form[f"V{i}"]) for i in range(1, 29)]

            input_data = np.array([[time] + pca_values + [amount]])
            pred = model.predict(input_data)[0]

            if pred == 0:
                status = "Legitimate"
                message = "✅ Transaction is Legitimate."
                color = "success"
            else:
                status = "Fraudulent"
                message = "🚨 Fraudulent Transaction Detected!"
                color = "danger"

            # Go to result page
            return render_template("result.html", status=status, message=message, color=color)

        except Exception as e:
            return render_template("result.html", status="Error", message=f"Error: {str(e)}", color="warning")

    return render_template("detect.html", title="Detection Page")

# if __name__ == "__main__":
#     app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)