from flask import Flask, render_template,redirect,request
from mypgfiles import fetch_data, insert_product, insert_sale, sales_per_day
import pygal


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
    return render_template('products.html', prods=prods)

@app.route("/sales")
def sales():
    sold=fetch_data("sales")
    return render_template('sales.html', sales=sold)

@app.route("/dashboards")
def dashboards():
    daily_sales = sales_per_day()
    dates = []
    sales =[]
    for i in daily_sales:
        dates.append(i[0])
        sales.append(i[0])
    print(sales)
    print(dates)
    chart = pygal.Line()
    chart.title = 'Sales per Day'
    chart.x_labels = dates
    # chart.y_labels = sales
    chart.add("Sales",sales)
    chart=chart.render_data_uri()
    return render_template("dashboard.html", chart=chart)
   


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
        print(product_id)
        print(quantity)
        sales= (product_id,quantity,"now()")
        insert_sale(sales)
        return redirect("/sales")

# @app.route("/register", methods=["GET","POST"])
# def register():
    


app.run(debug=True)
