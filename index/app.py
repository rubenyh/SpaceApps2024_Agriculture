from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # Get the search query from the URL
    if query:
        # Do something with the search query, for example:
        return render_template('search_results.html', query=query)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)