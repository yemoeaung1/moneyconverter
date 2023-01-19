from flask import Flask, request, render_template, redirect
import NumberConvert

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def convert():
    try:
        result = " "
        if request.method == "POST":
            amount = request.form.get("amount")
            result = NumberConvert.mainConvert(amount)
        return render_template("index.html", result = result)
    except ValueError():
        return redirect('index.html')

if __name__ == "__main__":
    app.run(debug=True)