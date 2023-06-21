from flask import Flask, render_template
from mypgfiles import fetch_data


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


app.run()
