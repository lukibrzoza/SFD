from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/request-counter' methods=['GET', 'POST'])
def request_counter():
    return


@app.route('/statistics')
def statistics():
    return

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
