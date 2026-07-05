import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    """
    Cleans resume text for machine learning.
    """

    # Lowercase
    text = text.lower()

    # Remove everything except letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Split into words
    words = text.split()

    cleaned_words = []

    for word in words:

        if word not in stop_words:

            word = lemmatizer.lemmatize(word)

            cleaned_words.append(word)

    cleaned_text = " ".join(cleaned_words)

    return cleaned_text