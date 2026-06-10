from db import get_connection

def get_by_rank(rank):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * WHERE soldiers rank = %s",(rank,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_active_sorted(order):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if order.lower() not in ("asc","desc"):
        order = "ASC"
    cursor.execute(f"SELECT * FROM soldiers WHERE active =  TRUE ORDER BY name {order.upper()}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_distinct_units():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT unit FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def search_by_name(term):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s",(f"%{term}%",))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_missing_rank():
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    cursor.execute("SELECT * FROM soldiers WHERE rank IS NULLL")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_by_unit(unit):
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    cursor.execute("SELECT * FROM soldiers WHERE unit = %s ORDER BY name ASC",(unit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
