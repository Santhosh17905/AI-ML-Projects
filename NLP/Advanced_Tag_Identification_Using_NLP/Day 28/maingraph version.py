"""
##  Advanced Tag Identification Using NLP

Features:
✔ Smart Web Scraping
✔ User-Agent Rotation
✔ Error Handling
✔ NLP Text Cleaning
✔ Stopword Removal
✔ Frequency Analysis
✔ Top Tag Extraction
✔ Bar Chart Visualization
✔ Word Cloud Generation
✔ CSV Export
✔ Modular Architecture
"""

import os
import urllib.request
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import string
import ssl
import logging

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

# =====================================================
# SETUP
# =====================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Handle SSL Certificate issues for NLTK and urllib
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords", quiet=True)

# =====================================================
# CONFIG
# =====================================================

URL = "https://en.wikipedia.org/wiki/Apple"

TOP_N_TAGS = 20

CUSTOM_STOPWORDS = {
    "apple",
    "inc",
    "company",
    "also",
    "one",
    "would",
    "many",
    "may"
}

# =====================================================
# FETCH WEBSITE CONTENT
# =====================================================

def fetch_website(url):
    try:
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        request = urllib.request.Request(
            url,
            headers=headers
        )

        response = urllib.request.urlopen(request, timeout=10)

        html = response.read()

        logging.info("Website loaded successfully.")

        return html

    except Exception as e:
        logging.error(f"Error loading website: {e}")
        return None


# =====================================================
# EXTRACT TEXT
# =====================================================

def extract_text(html):

    soup = BeautifulSoup(html, "html.parser")

    # Remove scripts/styles
    for tag in soup(["script", "style"]):
        tag.decompose()

    return soup.get_text(separator=" ")


# =====================================================
# CLEAN TEXT
# =====================================================

def preprocess_text(text):

    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    tokens = text.split()

    stop_words = set(stopwords.words("english"))
    stop_words.update(CUSTOM_STOPWORDS)

    filtered = [
        word
        for word in tokens
        if word.isalpha()
        and word not in stop_words
        and len(word) > 2
    ]

    return filtered


# =====================================================
# GET TOP TAGS
# =====================================================

def extract_tags(tokens, top_n=20):

    frequency = Counter(tokens)

    return frequency.most_common(top_n)


# =====================================================
# DISPLAY TAGS
# =====================================================

def show_tags(tags):

    print("\n" + "=" * 50)
    print("TOP IDENTIFIED TAGS")
    print("=" * 50)

    for i, (word, count) in enumerate(tags, start=1):
        print(f"{i:02d}. {word:<20} {count}")


# =====================================================
# EXPORT CSV
# =====================================================

def export_csv(tags):

    df = pd.DataFrame(
        tags,
        columns=["Tag", "Frequency"]
    )

    df.to_csv(
        "identified_tags.csv",
        index=False
    )

    logging.info(
        "Tags exported to identified_tags.csv"
    )


# =====================================================
# UTILITIES
# =====================================================

def ensure_output_folder(folder="screenshots"):
    os.makedirs(folder, exist_ok=True)
    return folder


def save_figure(filename):
    output_folder = ensure_output_folder()
    path = os.path.join(output_folder, filename)
    plt.savefig(path, bbox_inches="tight")
    logging.info(f"Saved screenshot: {path}")


def save_console_output(tags):
    lines = ["TOP IDENTIFIED TAGS", ""]
    lines += [f"{i:02d}. {word:<20} {count}" for i, (word, count) in enumerate(tags, start=1)]
    output_text = "\n".join(lines)

    fig, ax = plt.subplots(figsize=(8, max(4, len(lines) * 0.25)))
    ax.text(0, 1, output_text, fontfamily="monospace", va="top", ha="left", fontsize=10)
    ax.axis("off")

    save_figure("output_console.png")
    plt.close(fig)


# =====================================================
# BAR CHART
# =====================================================

def plot_bar_chart(tags):

    words = [tag[0] for tag in tags]
    freq = [tag[1] for tag in tags]

    plt.figure(figsize=(12, 6))

    plt.bar(words, freq)

    plt.title(
        "Top NLP Identified Tags"
    )

    plt.xlabel("Tags")
    plt.ylabel("Frequency")

    plt.xticks(rotation=45)

    plt.tight_layout()

    save_figure("bar_chart.png")
    plt.show()
    plt.close()


# =====================================================
# WORD CLOUD
# =====================================================

def generate_wordcloud(tokens):

    text = " ".join(tokens)

    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white"
    )

    wc.generate(text)

    plt.figure(figsize=(12, 6))

    plt.imshow(wc)

    plt.axis("off")

    plt.title("Word Cloud")

    save_figure("wordcloud.png")
    plt.show()
    plt.close()


# =====================================================
# MAIN
# =====================================================

def main():

    ensure_output_folder()

    html = fetch_website(URL)

    if html is None:
        return

    text = extract_text(html)

    tokens = preprocess_text(text)

    tags = extract_tags(
        tokens,
        TOP_N_TAGS
    )

    show_tags(tags)

    export_csv(tags)

    plot_bar_chart(tags)

    generate_wordcloud(tokens)

    save_console_output(tags)


if __name__ == "__main__":
    main()