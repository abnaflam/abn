from flask import Flask, Response
import requests

app = Flask(__name__)

SOURCE_M3U8 = "https://kid-3bk.pages.dev/mbein/bein1.m3u8"

@app.route("/bein1.m3u8")
def restream():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://kid-3bk.pages.dev/"
    }

    r = requests.get(SOURCE_M3U8, headers=headers, stream=True, timeout=10)

    return Response(
        r.iter_content(chunk_size=1024),
        content_type="application/vnd.apple.mpegurl"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
