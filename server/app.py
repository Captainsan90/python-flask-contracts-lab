from flask import Flask

app = Flask(__name__)

# In-memory data
contracts = {
    "1": "This contract is for John and building a shed"
}

customers = {
    "bob": True  # exists but returns no data (sensitive)
}

# Route: GET /contract/<id>
@app.route('/contract/<id>', methods=['GET'])
def get_contract(id):
    if id in contracts:
        return contracts[id], 200
    return "Not found", 404


# Route: GET /customer/<customer_name>
@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    if customer_name in customers:
        return "", 204
    return "Not found", 404


if __name__ == '__main__':
    app.run(debug=True)