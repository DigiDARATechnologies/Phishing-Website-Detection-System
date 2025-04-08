from flask import Flask, render_template, request
import pickle
import numpy as np
from extract_features import extract_features

# Load model
print("Attempting to load phishing_model.pkl...")
try:
    with open("phishing_model.pkl", "rb") as f:
        model = pickle.load(f)
    # Get expected feature count from the first estimator
    expected_features = len(model.estimators_[0].feature_names_in_) if hasattr(model.estimators_[0], 'feature_names_in_') else 30
    print(f"Model loaded successfully. Expected features: {expected_features}")
except FileNotFoundError:
    print("Error: phishing_model.pkl not found. Please train and save the model.")
    raise
except Exception as e:
    print(f"Error loading model: {str(e)}")
    raise

app = Flask(__name__)

@app.route('/')
def home():
    print("Rendering home page...")
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    print("Processing predict request...")
    try:
        url = request.form.get('url', '')
        if not url:
            return render_template("index.html", prediction="❌ No URL provided.", input_url="", extra_info="")
        
        features, message = extract_features(url)
        features = np.array(features).reshape(1, -1)
        
        # Validate feature count
        print(f"Extracted feature count: {features.shape[1]}")
        if features.shape[1] != expected_features:
            return render_template("index.html", 
                                  prediction=f"❌ Feature mismatch: Expected {expected_features}, got {features.shape[1]}", 
                                  input_url=url, 
                                  extra_info=message)
        
        prediction = model.predict(features)[0]
        result = "🚫 Phishing Website" if prediction == 1 else "✅ Legitimate Website"
        print(f"Prediction: {result} for URL: {url}")
        return render_template("index.html", prediction=result, input_url=url, extra_info=message)
    
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return render_template("index.html", prediction=f"❌ Error: {str(e)}", input_url=url, extra_info=message)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='0.0.0.0', port=5000)