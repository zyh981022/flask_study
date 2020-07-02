from flask import Flask
app = Flask(__name__)



@app.route('/<name>')
def index(name):
    return '<h1>Hello,%s Flask!</h>'%name




#print(app.name)


#app.run()


