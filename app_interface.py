from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import FashionProduct
import config
import traceback


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"result":"Successful"})
    # return render_template('index.html')

@app.route('/predict_price', methods=['GET','POST'])
def predict_price():
    try:
        if request.method == 'POST':
            data = request.form
            print({"DATA": data})
        elif request.method == 'GET':
            data = request.form
            print({"DATA": data})

        product_name = data['product_name']
        brand = data['brand']
        category = data['category']
        rating = eval(data['rating'])
        size = data['size']
        color = data['color']

        obj = FashionProduct(product_name,brand,category,rating,size,color)
        pred_price = obj.get_predicted_charges()
        return jsonify({"result":pred_price})
        # return render_template('index.html', prediction = pred_price)
    except:
        print(traceback.print_exc())
        # return redirect(url_for('home'))
        return jsonify({"result": "Failed"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port= config.PORT_NUMBER)