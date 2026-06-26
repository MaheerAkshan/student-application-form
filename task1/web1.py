from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = age = department = college = ""

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        department = request.form["department"]
        college = request.form["college"]

    return render_template(
        "index.html",
        name=name,
        age=age,
        department=department,
        college=college
    )

if __name__ == "__main__":
    app.run(debug=True)