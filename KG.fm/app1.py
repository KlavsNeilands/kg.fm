from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    page_title = "About"
    return render_template('about.html', page_title=page_title)

@app.route('/browse')
def browse():
    page_title = "Browse"
    return render_template('browse.html', page_title=page_title)

@app.route('/newreleases')
def newreleases():
    page_title = "New releases"
    return render_template('newreleases.html', page_title=page_title)

@app.route('/recommended')
def recommended():
    page_title = "Recommended"
    return render_template('recommended.html', page_title=page_title)

if __name__ == '__main__':
    app.run(debug=True)






