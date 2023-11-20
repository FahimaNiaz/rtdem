from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # In a real application, fetch data and pass it to the template
    data = {
        'graph1': 'url_to_graph1_image',
        'graph2': 'url_to_graph2_image',
        # Add more graph URLs as needed
    }
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
