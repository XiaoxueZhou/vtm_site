from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        print(radius)
        print(height)
        TankTop = 3.14 * radius * radius
        TankSide = 3.14 * radius * height
        TotalArea = TankTop + TankSide
        Totalsf = TotalArea / 144
        MaterialCost = Totalsf * 25
        LabotCost = Totalsf * 15
        TotalCost = (round(MaterialCost + LabotCost))
        return render_template('estimate.html', calculate=TotalCost)
    return render_template('estimate.html',pageTitle='Estimate')

if __name__ == '__main__':
    app.run(debug=True)