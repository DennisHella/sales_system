import psycopg2


try:
    conn = psycopg2.connect("dbname=duka_june user=postgres password=12345")
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
    q = "insert into products(name,buying_price,selling_price,stock_quantity) "\
        "values"+ vs
    cur.execute(q)
    conn.commit()
    return "Product Successfully Added."

def fetch_last_data(tbln):
    try:
        q = "SELECT * FROM " + tbln + " ORDER BY id desc LIMIT 1;"
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e