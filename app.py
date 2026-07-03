from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and label encoders
model = joblib.load("placement_model.pkl")
encoders = joblib.load("encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        gender = request.form["gender"]
        ssc_p = float(request.form["ssc_p"])
        ssc_b = request.form["ssc_b"]
        hsc_p = float(request.form["hsc_p"])
        hsc_b = request.form["hsc_b"]
        hsc_s = request.form["hsc_s"]
        degree_p = float(request.form["degree_p"])
        degree_t = request.form["degree_t"]
        workex = request.form["workex"]
        etest_p = float(request.form["etest_p"])
        specialisation = request.form["specialisation"]
        mba_p = float(request.form["mba_p"])

        # Encode categorical values
        gender = encoders["gender"].transform([gender])[0]
        ssc_b = encoders["ssc_b"].transform([ssc_b])[0]
        hsc_b = encoders["hsc_b"].transform([hsc_b])[0]
        hsc_s = encoders["hsc_s"].transform([hsc_s])[0]
        degree_t = encoders["degree_t"].transform([degree_t])[0]
        workex = encoders["workex"].transform([workex])[0]
        specialisation = encoders["specialisation"].transform([specialisation])[0]

        input_data = pd.DataFrame([[
            gender,
            ssc_p,
            ssc_b,
            hsc_p,
            hsc_b,
            hsc_s,
            degree_p,
            degree_t,
            workex,
            etest_p,
            specialisation,
            mba_p
        ]], columns=[
            "gender",
            "ssc_p",
            "ssc_b",
            "hsc_p",
            "hsc_b",
            "hsc_s",
            "degree_p",
            "degree_t",
            "workex",
            "etest_p",
            "specialisation",
            "mba_p"
        ])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "🎉 Student is Likely to be PLACED"
        else:
            result = "❌ Student is NOT Likely to be Placed"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)