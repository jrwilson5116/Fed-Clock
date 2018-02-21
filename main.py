from time_keeper import get_time_decimal, over_under,get_minutes
from flask import Flask, request



app = Flask(__name__)
app.config['DEBUG']=True


form = """
<!DOCTYPE html>



<html>

    <head>
        <header>
            <h1> Fed Clock  </h1>
        </header>
        <style>
         
            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            h1 {{
                font: 80px sans-serif;
                
                padding: 20px;

                margin: 0 auto;

                width: 540px;

                border-radius: 10px;

                color: #483D8B


            }}

            footer {{
                padding: 20px;

                margin: 0 auto;

                width: 540px;

                border-radius: 10px;
            }}

        </style>

    </head>

    <body>

		<form action = "/" method = "post">
			Time in: 
			<input name ="time_in" type ="text" value = 0>
            Hours Worked:
            <input name = "time_worked" type = "text" value = {0}>
			<br><br>
            Time out:
			<input name = "time_out" type ="text" value = 0>
            Over/Under:
            <input name = "over_under" typer = "text" value = {1}>
			<br><br>
			<input type ="submit">
            <input type = "reset" value = "Clear fields">
    
		</form>


    </body>
    <footer>
    version 1.1<br>
    created by: Joey Wilson
    </footer>
</html>
    """

@app.route("/")
def index():
    return form.format("","")


@app.route("/",methods = ['POST'])
def calculate():
    clock_in= request.form['time_in']
    clock_out=request.form['time_out']
    total = get_time_decimal(clock_in,clock_out)
    over = over_under(total)
    return form.format(total,over)


if __name__=="__main__":
    app.run(debug=True, use_reloader=True)