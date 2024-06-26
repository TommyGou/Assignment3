from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return '{ name: "Tongfei Gou", id: 200551009 }'


@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'get.address':
        ### Perform set of executable code
        ### if required
        ### ...
        fulfillmentText = 'Hi'
    return{
        'fulfillmentText':fulfillmentText,
        'source':'webhookdata'
    }

# run the app
if __name__ == '__main__':
    app.run()



