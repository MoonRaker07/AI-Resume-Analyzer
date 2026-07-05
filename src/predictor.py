import joblib
from src.preprocessing import preprocess_text

# Load models
tfidf = joblib.load("models/tfidf.pkl")
classifier = joblib.load("models/classifier.pkl")


def predict_resume_category(resume_text):

    cleaned_text = preprocess_text(resume_text)

    vector = tfidf.transform([cleaned_text])

    prediction = classifier.predict(vector)[0]

    return prediction