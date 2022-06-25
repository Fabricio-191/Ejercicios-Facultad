from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

import src.database
import src.compartirRecetas
import src.consultarRecetas
import src.login

if __name__ == '__main__':
    app.run(debug=True)
