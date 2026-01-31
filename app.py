import os
import requests
from flask import Flask, Response

app = Flask(__name__)

SOURCE = "https://kid-3bk.pages.dev/mbein/bein1.m3u8"

@app.route("/bein1.m3u8")
def stream():
    r = requests.get(SOURCE, stream=True)
    return Response(
        r.iter_content(1024),
        content_type="application/vnd.apple.mpegurl"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)
