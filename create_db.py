import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="12345")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS portfolio_db")
    print("Database 'portfolio_db' created successfully.")
except Exception as e:
    print(f"Failed to create database: {e}")
finally:
    if 'db' in locals():
        db.close()
