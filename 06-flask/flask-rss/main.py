
import feedparser
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    feed = feedparser.parse(r'http://www.prweb.com/rss2/daily.xml')

    df = pd.json_normalize(feed.entries, sep='_')

    df['source'] = "prweb"

    df = df.sort_values('published', ascending=False)

    df = df[['published', 'link', 'title','source']]

    return render_template("reader.html", df=df.itertuples(), columns_to_display=['published', 'Source', 'Headline'])

@app.route("/")
def data():

    df = pd.read_csv(r'../data/')

    df['source'] = "prweb"

    df = df.sort_values('published', ascending=False)

    df = df[['published', 'link', 'title','source']]

    return render_template("table.html", df=df.itertuples(), columns_to_display=['published', 'Source', 'Headline'])

if __name__ == "__main__":
    app.run(debug=True)
