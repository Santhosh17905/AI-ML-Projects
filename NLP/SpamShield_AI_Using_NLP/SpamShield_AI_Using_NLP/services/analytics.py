# Analytics service placeholder
from wordcloud import WordCloud

def generate_wordcloud(text):

    wc = WordCloud(
        width=800,
        height=400
    )

    wc.generate(text)

    wc.to_file(
        "static/charts/wordcloud.png"
    )

    return "static/charts/wordcloud.png"