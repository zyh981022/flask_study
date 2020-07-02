from flask import Flask
app = Flask(__name__)



@app.route('/<name>')
@app.route('/',defaults={'name':'zyh'})
def index(name):
    return '<h1>Hello,%s Flask!</h>'%name




#print(app.name)

"888"
#app.run()


