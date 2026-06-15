# Tag Identification using NLP
# Solution 1: urllib with User-Agent

import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# Download stopwords (first time only)
nltk.download('stopwords')

# -------------------------------
# STEP 1: Fetch Website Content
# -------------------------------

url = "https://en.wikipedia.org/wiki/Apple"

headers = {
    "User-Agent": "Mozilla/5.0"
}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html = response.read()

print("✅ Website loaded successfully!\n")

# -------------------------------
# STEP 2: Extract Text from HTML
# -------------------------------

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

# -------------------------------
# STEP 3: Text Cleaning
# -------------------------------

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenization (split into words)
tokens = text.split()

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words and word.isalpha()]

# -------------------------------
# STEP 4: Find Most Frequent Words (Tags)
# -------------------------------

word_freq = Counter(filtered_words)

# Get top 10 most common words
top_tags = word_freq.most_common(10)

print("🔥 Top Suggested Tags:\n")
for word, freq in top_tags:
    print(f"{word}  -->  {freq} times")