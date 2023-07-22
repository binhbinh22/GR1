from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Lấy dữ liệu từ cơ sở dữ liệu
    cursor.execute("SELECT title, point, title_href, time FROM news")
    news = cursor.fetchall()

    # Đóng kết nối cơ sở dữ liệu
    cursor.close()
    conn.close()

    # Trả về trang web với dữ liệu tin tức
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run()
