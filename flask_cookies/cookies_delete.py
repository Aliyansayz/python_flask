Deleting a Cookie:
To delete a cookie, you can set its expiration time to a value in the past. This will prompt the client's browser to remove the cookie.

python

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Deleting a cookie!')
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run()

In this example, setting the expires parameter to 0 ensures that the cookie is expired and will be removed by the browser.
