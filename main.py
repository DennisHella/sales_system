from flask import Flask, render_template,redirect,request
from mypgfiles import fetch_data, insert_product, insert_sale


# # # Create object called app
# # #  Object is used to access sth inside a class
# # # _name_ is used to tell Flask where to access HTML Files
# # #  All HTML files are put inside a "templates" folder
# # #  All CSS/JS/Images are put inside "static" folder
app = Flask(__name__)



# # # A route is an extension of a url which loads you an HTML image.
# # # @ binds a route it to  function

@app.route("/")
def home():
    hella= "Dennis"
    return render_template("index.html", x=hella )

@app.route("/products")
def products():
    prods=fetch_data("products")
    return render_template('products.html', products=prods)

@app.route("/sales")
def sales():
    sold=fetch_data("sales")
    return render_template('sales.html', sales=sold)

@app.route("/add_products", methods=["POST","GET"])
def add_products():
    if request.method == "POST":
        name=request.form["name"]
        buying_price=request.form["buying_price"]
        selling_price=request.form["selling_price"]
        stock_quantity=request.form["stock_quantity"]
        print(name)
        print(buying_price)
        print(selling_price)
        print(stock_quantity)
        product = (name,buying_price,selling_price,stock_quantity)
        insert_product(product)
        return redirect("/products")
    
    
@app.route("/add_sales", methods=["POST","GET"])
def add_sales():
    if request.method == "POST":
        product_id=request.form["product_id"]
        quantity=request.form["quantity"]
        time_created=request.form["created_at"]
        print(product_id)
        print(quantity)
        print(time_created)
        sales= (product_id,quantity,time_created)
        insert_sale(sales)
        return redirect("/sales")





app.run(debug=True)
