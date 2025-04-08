
# Phishing Website Detection System

## Overview

The **Phishing Website Detection System** is an educational tool designed to classify URLs as phishing or legitimate using machine learning. Built with **Python**, **Flask**, and **scikit-learn**, this project trains a model on a phishing dataset and provides a web interface to test URL predictions. It’s intended for cybersecurity education, allowing users to explore phishing detection techniques in a controlled environment.

---

## Features

- 🌐 Web-based interface to input URLs and receive instant predictions  
- 🤖 Machine learning model trained with a `VotingClassifier` ensemble (Random Forest and XGBoost)  
- 🧩 Feature extraction from URLs based on structural and domain information  
- 🛠️ Debug output for troubleshooting and learning  
- 🔧 Extensible design for adding new features or models  

---

## Prerequisites

- Python 3.8+

### Required Python libraries:

```bash
flask  
scikit-learn  
xgboost  
numpy  
pandas  
requests  
whois  
pickle
```

Optional: IPQualityScore API key for IP reputation checks (replace in `extract_features.py`)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phishing-detection.git
cd phishing-detection
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Create a `requirements.txt` file with the following content:

```text
flask==2.3.2  
scikit-learn==1.2.2  
xgboost==1.7.5  
numpy==1.24.3  
pandas==2.0.1  
requests==2.28.1  
python-whois==0.8.0
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Dataset

- Place your `phishing.csv` file in the project directory.
- Ensure it contains URL features and a `class` column (e.g., `-1` for legitimate, `1` for phishing).
- Confirm column names match the training script’s expectations.

### 5. Obtain an API Key (Optional)

- Sign up at [ipqualityscore.com](https://www.ipqualityscore.com/) for an API key.  
- Replace the placeholder `API_KEY` in `extract_features.py` with your key.

---

## Usage

### 1. Train the Model

Run the training script:

```bash
python train_model.py
```

Output:

- Checks for `phishing.csv`
- Trains the model
- Prints feature names and accuracy
- Saves model as `phishing_model.pkl`

_Note: Review console output for the number of features to adjust `extract_features.py` if needed._

### 2. Run the Web Application

Start the Flask server:

```bash
python app.py
```

Open a browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

- Enter a URL (e.g., `https://www.google.com`) and submit.
- Displays a prediction:
  - ✅ Legitimate Website
  - 🚫 Phishing Website

### 3. Debug and Test

- Check console for debug prints (e.g., feature count, prediction).
- Try known phishing and legitimate URLs to evaluate model accuracy.

---

## File Structure

```
phishing-detection/
│   README.md
│   requirements.txt
│   app.py              # Flask application
│   train_model.py      # Model training script
│   extract_features.py # Feature extraction logic
│   phishing.csv        # Dataset (place here)
│   phishing_model.pkl  # Trained model (generated)
│
└───templates/
    │   index.html      # Web interface template
```

---

## Configuration

- **API Key**: Update `API_KEY` in `extract_features.py` (optional).
- **Feature Count**: Adjust padding in `extract_features.py` to match output from `train_model.py`.
- **Port**: Default is 5000. Change it in `app.py` if needed.

---

## Contributing

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes  
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch  
   ```bash
   git push origin feature-name
   ```
5. Open a pull request

_Suggestions: Add new features, improve UI, or enhance model accuracy._

---
