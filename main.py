from flask import Flask, render_template
import psycopg2
from mypgfiles import fetch_data


# # Create object called app
# #  Object is used to access sth inside a class
# # _name_ is used to tell Flask where to access HTML Files
# #  All HTML files are put inside a "templates" folder
# #  All CSS/JS/Images are put inside "static" folder
app = Flask(__name__)

conn=psycopg2.connect(host='localhost', database='myduka',user='postgres',password='Dennis97')
cur=conn.cursor()


# # A route is an extension of a url which loads you an HTML image.
# # @ binds a route it to  function

# @app.route("/")
# def home():
#     return render_template("index.html")

# query='SELECT * FROM products'
# cur.execute(query)
# records=cur.fetchall()
# print("Select data is:\n",)
# for record in records:
#     print(record)
# print()

# app.run()

from flask import Flask, render_template
import psycopg2

app=Flask(__name__)

conn=psycopg2.connect(host='localhost', database='myduka',user='postgres',password='Dennis97')
cur=conn.cursor()

query='SELECT * FROM products'
cur.execute(query)
records=cur.fetchall()
print("Select data is:\n",)
for record in records:
    print(record)
print()


conn.commit()
conn.close()
cur.close()

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
