from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def count_words():
    count = ""

    if request.method == "POST":
        paragraph = request.form['paragraph']
        count = len(paragraph.split())

    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)