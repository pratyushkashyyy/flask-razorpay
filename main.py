from flask import Flask,render_template,redirect,request
import razorpay

app = Flask(__name__)
client = razorpay.Client(auth=("rzp_test_I4RI6OLrPcJeSM", "O0bjtxZVNQNNLbrLwOfL6p4E"))

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        amount = request.form.get("amount")
        if not  amount:
            return "Amount cannot be empty !!", 400
        try:
            amount = float(amount)
        except ValueError:
            return "Enter an Valid Amount", 400
        amount = amount * 100
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        pdata=[amount, payment["id"]]
        return render_template('index.html', amount=amount)
    if request.method == "GET":
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)