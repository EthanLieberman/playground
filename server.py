from flask import Flask, render_template


app = Flask(__name__)

@app.route('/') # this is what is typed into the browser http://localhost:5000/ <- base route
def hello_world():
    print("this is showing a request on '/'")
    return render_template('index.html', phrase="hi there", times=3)



@app.route('/play')
def play():
    print("this is showing a request on '/play'")
    return render_template('index.html', times=3, color=0)

@app.route('/play/<int:num>')
def play_num(num):
    print("this is showing a request on '/play'")
    return render_template('index.html',times=num, color=0)


@app.route('/play/<int:num>/<string:color>')
def play_color(num, color):
    print("this is showing a request on '/play'")
    return render_template('index.html',times=num, color=color)







if __name__ == "__main__":
    app.run(debug = True)