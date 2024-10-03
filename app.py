from flask import Flask, request
from flask_cors import CORS
from Shopping import Shoppping
from Groceries import Groceries

app = Flask(__name__)
CORS(app)

# Initialize productName with "books"
productName = "books"

# Initialize groceriesName with "milk"
groceriesName = "milk"

@app.route('/api/v1/shopping')
def hello_world():
    global productName  # Reference the global variable productName
    shopping = Shoppping(productName)
    return shopping.amazonShopping()

@app.route('/api/v1/groceries')
def groceries_api_index():
    global groceriesName
    groceries = Groceries(groceriesName)
    return groceries.groceries_api()

@app.route('/api/v1/search/shopping', methods=['POST'])
def search_shopping():
    data = request.get_json()
    global productName

    if data and isinstance(data, str) and data.strip():  # Check if data is not empty or null
        productName = data
    else:
        productName = "books"  # Set productName to "books" if data is empty or null

    print(productName)
    return data

@app.route('/api/v1/search/groceries', methods=['POST'])
def search_groceries():
    data = request.get_json()
    global groceriesName

    if data and isinstance(data, str) and data.strip():
        groceriesName = data
    else:
        groceriesName = 'milk'
    print(groceriesName)
    return data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
