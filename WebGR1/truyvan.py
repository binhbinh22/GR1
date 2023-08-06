import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('database.db')

# Tạo đối tượng cursor
cursor = conn.cursor()

# Thực hiện truy vấn SQL và lấy dữ liệu
cursor.execute('SELECT * FROM news')
data = cursor.fetchall()

# In dữ liệu
for row in data:
    print(row)

# Đóng kết nối
conn.close()
