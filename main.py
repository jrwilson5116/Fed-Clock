from time_keeper import get_time_decimal, over_under,format_time
from flask import Flask, request, render_template, redirect,url_for,flash


app = Flask(__name__)
app.config['DEBUG']=True
app.secret_key='abcdefg'


@app.route("/")
def index():
    return render_template('index.html').format("","")


@app.route("/",methods = ['POST'])
def calculate():
    clock_in = request.form['time_in']
    clock_out = request.form['time_out']
    if format_time(clock_out) < format_time(clock_in):
        flash("Invalid times, clock out must come AFTER clock in")
        return redirect(url_for('index'))
    else:
        total = get_time_decimal(clock_in,clock_out)
        over = over_under(total)
        return render_template('index.html').format(total,over)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True, use_reloader=True)