from flask import Flask, request, render_template
import NumberConvert

app = Flask(__name__)
    

@app.route("/", methods = ["GET", "POST"])
def convert():
    if request.method == "POST":
        amount = request.form.get("amount")
        print(amount)
        return NumberConvert.mainConvert(amount)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)