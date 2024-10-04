"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("US_births_DB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM US_births_DB")
    cursor.execute(
        """
            INSERT INTO US_births_DB (year, month, date_of_month, day_of_week, births) 
            VALUES (2008, 8, 8, 1, 9999)""",
    )
    cursor.execute(
        """
            UPDATE US_births_DB 
            SET day_of_week = 1, births = 6666
            WHERE id = 1""",
    )
    cursor.execute(
        """
            DELETE FROM US_births_DB 
            WHERE id = 2""",
    )
    print("Top 5 rows of the US_births_DB table:")
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    return "Success"
