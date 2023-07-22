import sqlite3

def query_all_tables(db_file):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Lấy danh sách các bảng trong cơ sở dữ liệu
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    # Truy vấn và in dữ liệu từ các bảng
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
    
    # Đóng kết nối cơ sở dữ liệu
    cursor.close()
    conn.close()

# Gọi hàm để truy vấn và xem tất cả bảng trong cơ sở dữ liệu
db_file = 'database.db'  # Tên file cơ sở dữ liệu SQLite

query_all_tables(db_file)
