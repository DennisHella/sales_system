import psycopg2


try:
    conn =psycopg2.connect(host='localhost', database='myduka',user='postgres',password='Dennis97')   
    cur = conn.cursor()
except Exception as e:
    print(e)

def fetch_data(tbln):
    try:
        q = "SELECT * FROM " + tbln + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e
    
def insert_product(v):
    vs = str(v)
    q = "insert into products(name,buying_price,selling_price,quanttity) "+"values"+ vs
    cur.execute(q)
    conn.commit()
    return "Product Successfully Added."

def insert_sale(s):
    vs = str(s)
    q = "insert into sales(pid,quantity,created_at) "+"values"+ vs
    cur.execute(q)
    conn.commit()
    return "Sale Successfully Added."

def sales_per_day():
    q= "Select created_at,SUM(quantity) as total_sales from sales GROUP BY created_at ORDER BY created_at"
    cur.execute(q)
    results=cur.fetchall()
    return results

def fetch_last_data(tbln):
    try:
        q = "SELECT * FROM " + tbln + " ORDER BY id desc LIMIT 1;"
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e