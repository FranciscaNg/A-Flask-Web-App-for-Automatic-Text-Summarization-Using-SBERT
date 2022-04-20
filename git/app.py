#importing flask
from flask import Flask, render_template,request
#Importing the summarizer
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

# Using an instance of SBERT to create the model
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)# If you want to know which URL should be used to call the associated method, use the route() function of Flask's class. The URL binding with the function is represented by the rule's rule argument.

@app.route("/")#In this case, mapping the URLs to a function that will handle the logic for each individual URL
def msg():
    # Giving a result
    return render_template('index.html')
    
@app.route("/summarize",methods=['POST','GET'])# If the gateway is unable to obtain the client's IP address, this information will be missing from the request.
def getSummary():
    body=request.form['data']# Sending a request
    result = model(body, num_sentences=5)# Defining instances
    return render_template('summary.html',result=result)
    
if __name__ =="__main__":# When modules are imported, it allows or deny certain code to be executed.
    app.run(debug=True,port=8000)#IP address on which a Web client can communicate with the server.