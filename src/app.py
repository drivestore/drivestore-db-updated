from flask import Flask,redirect,request
import os

app = Flask(__name__)

ENV_PUSH_KEY = os.environ["PUSH_KEY"]


@app.route("/<PUSH_KEY>")
def default(PUSH_KEY):
    if(ENV_PUSH_KEY == PUSH_KEY):
        return 'LOADING FILE / INJECTING WITH COPY '
    else :
        return "404"

@app.route("/key")
def key(PUSH_KEY):
    return 'KEY : '+str(ENV_PUSH_KEY)

@app.errorhandler(404)
def error404(e):
    # note that we set the 404 status explicitly
    return "404", 404

@app.errorhandler(500)
def error500(e):
    # note that we set the 500 status explicitly
    return "500", 500
    
# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)