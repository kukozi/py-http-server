from flask import Flask, request, abort, current_app as app
from src.ipban import ip_ban_list
import src.serverconfig as srv

app = Flask(__name__)

@app.before_request
def block_method():
    ip_ban = request.environ.get('REMOTE_ADDR')
    if ip_ban in ip_ban_list:
        abort(418)

@app.route("/")
def index():
    return (
            """
            <html>
                <head>
                    <link rel="icon" type="image/png" href="/static/favicon.ico">
                </head>
                <script src="https://cdn.logwork.com/widget/countdown.js"></script>
                <a href="https://logwork.com/countdown-xgow" class="countdown-timer" data-timezone="Europe/Moscow" data-date="2023-01-22 13:30" onclick="return false">Countdown Timer</a>
            </html>
            """
    )

if __name__ == "__main__":
    urls = (
        '/', 'index',
        '/src/favicon.ico', 'icon'
    )
    app.run(host= srv.ip, port=srv.port, debug=True)