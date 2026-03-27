# Assignment: Build a Text Cleaner
# Date: 21/03/2026
# Objective: Write code to remove punctuation, lowercase text
# remove stopwords and test it.


import nltk
from nltk.corpus import stopwords
import string

# Download resources (first time only)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))

def text_cleaner(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    words = nltk.word_tokenize(text)
    # Remove stopwords
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Test
sample = "OMG this is sooo coool!!!"
print("Original:", sample)
print("Cleaned :", text_cleaner(sample))