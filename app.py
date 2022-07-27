from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','Post'])
def index():
    return "Starting Stores Sales Prediction project"

if __name__=="__main__":
    app.run(debug=True)

