from flask import Flask, render_template

app = Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        myClass = request.form['myClass']

        return render_template('myClass.html', myClass = myClass)
    return render_template('index.html')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# "debug=True" is used so you don't have to restart server in terminal
