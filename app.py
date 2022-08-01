import sys
from flask import Flask
from sales.logger import logging
from sales.exception import SalesException
app=Flask(__name__)



@app.route("/",methods=['GET','Post'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        sal = SalesException(e,sys)
        logging.info(sal.error_message)
        logging.info("we are testing logging module")
    return "Starting Stores Sales Prediction project"

if __name__=="__main__":
    app.run(debug=True)

