from flask import Flask, render_template
app = Flask(__name__)
from controllers.sources_controller import sources_blueprint
from controllers.sounds_controller import sounds_blueprint

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(sources_blueprint)
app.register_blueprint(sounds_blueprint)
