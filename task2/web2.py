from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""

    if request.method == "POST":
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['operation']

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)