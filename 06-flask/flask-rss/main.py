import os
from datetime import datetime

import feedparser
import pandas as pd
from flask import Flask, render_template

pd.set_option("display.float_format", lambda x: "%.5f" % x)  # pandas
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 600)

pd.set_option('expand_frame_repr', True)
pd.set_option('max_rows', 50)
pd.set_option('display.max_rows', 50)

featured = {
    "prweb": "http://www.prweb.com/rss2/daily.xml"
}


def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", featured=featured)


@app.route("/reader/", methods=["POST", "GET"])
@app.route("/reader/<source>", methods=["POST", "GET"])
def readerPage(source=None):
    try:

        feed = feedparser.parse(r'http://www.prweb.com/rss2/daily.xml')

        keep = ['published', 'link', 'title']

        _entries = []

        for entry in feed.entries:
            # final_dict = {key: entry[key] for key in entry.keys() if key in keep}
            final_dict = flatten(entry)

            _entries.append(final_dict)

        df = pd.DataFrame(_entries)

        df = df.sort_values('published', ascending=False)

        df['source'] = "prweb"

        df = df[['published', 'link', 'title','source']]

        data_dir = os.path.join(os.getcwd(), "data")

        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        # df.to_csv(os.path.join(data_dir, f"headlines_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"))

        return render_template("reader.html", name=source, df=df.itertuples(), cols=keep)

    except Exception as e:
        return render_template("reader.html", name=source, error=e)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("notfound.html", featured=featured), 404


if __name__ == "__main__":
    app.run(debug=True)
