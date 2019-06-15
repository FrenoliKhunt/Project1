from flask import Flask, render_template, request
import os

app = Flask(__name__)



# port = int(os.getenv("VCAP_APP_PORT"))
port = os.getenv("VCAP_APP_PORT")


@app.route('/')
def index():

    return render_template("fgk_8950.html")





if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=port)

