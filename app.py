from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        radius = float(request.form.get('radius'))
        area = 3.14 * radius ** 2  # Using π approximated to 3.14
        return render_template('circle.html', area=area)
    return render_template('circle.html')

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    if request.method == 'POST':
        base = float(request.form.get('base'))
        height = float(request.form.get('height'))
        area = 0.5 * base * height
        return render_template('triangle.html', area=area)
    return render_template('triangle.html')

@app.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    if request.method == 'POST':
        width = float(request.form.get('width'))
        height = float(request.form.get('height'))
        area = width * height
        return render_template('rectangle.html', area=area)
    return render_template('rectangle.html')

if __name__ == '__main__':
    app.run(debug=True)

