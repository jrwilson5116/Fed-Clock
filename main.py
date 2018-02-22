from time_keeper import get_time_decimal, over_under
from flask import Flask, request, render_template


app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('index.html').format("","")


@app.route("/",methods = ['POST'])
def calculate():
    error = None
    clock_in = request.form['time_in']
    clock_out = request.form['time_out']
    if not sum(i.isdigit() for i in clock_in)>=3 or \
        not sum(e.isdigit() for e in clock_out)>=3:
            error = 'Please enter a valid time!'
            return render_template('index.html').format("","")
    else:
        total = get_time_decimal(clock_in,clock_out)
        over = over_under(total)
        return render_template('index.html').format(total,over)


if __name__=="__main__":
    app.run(debug=True, use_reloader=True)