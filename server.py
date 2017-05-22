from flask import Flask, render_template, request, abort
from typograph import Typograph

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        input_text = request.form['text']
        typographed_text = Typograph(input_text).typographed_text
        return render_template('form.html', result=typographed_text, origin=input_text)

if __name__ == "__main__":
    app.run(debug=True)
