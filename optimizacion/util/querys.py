from django.db import connection

def prod_by_abrev():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM producto_caracteristica WHERE abreviatura = 'NR'")
        row =dictfetchall(cursor)
    return row

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def prod_by_ids(sql):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM producto_caracteristica WHERE id in %s", [sql])
        row =dictfetchall(cursor)
    return row
