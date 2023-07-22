import csv
import sqlite3

def create_table_from_csv(csv_file, table_name, db_file):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Đọc file CSV và lấy danh sách tên cột
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        header = csv_reader.fieldnames

        # Xây dựng câu lệnh SQL CREATE TABLE
        columns = ", ".join([f"{column} TEXT" for column in header])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

        # Tạo bảng trong cơ sở dữ liệu
        cursor.execute(create_table_query)

        # Xây dựng câu lệnh SQL INSERT để chèn dữ liệu vào bảng
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(header))})"

        # Đọc từng dòng trong file CSV và chèn dữ liệu vào bảng
        for row in csv_reader:
            values = [row[column] for column in header]
            cursor.execute(insert_query, values)

    # Lưu các thay đổi và đóng kết nối cơ sở dữ liệu
    conn.commit()
    cursor.close()
    conn.close()

# Gọi hàm để tạo bảng và chèn dữ liệu từ file CSV
csv_file = 'point_title.csv'  # Đường dẫn đến file CSV của bạn
table_name = 'news'  # Tên bảng trong cơ sở dữ liệu
db_file = 'database.db'  # Tên file cơ sở dữ liệu SQLite

create_table_from_csv(csv_file, table_name, db_file)
