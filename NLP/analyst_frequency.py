import pandas as pd
from collections import Counter

# Đường dẫn đến file CSV
csv_file_path = "ketqua.csv"

# Đọc dữ liệu từ file CSV
data_frame = pd.read_csv(csv_file_path)

# Trích xuất cột "title"
titles = data_frame["entity"].tolist()

# Tính tần suất từ
word_counts = Counter()
for title in titles:
    words = title.split()  # Tách câu thành các từ
    word_counts.update(words)

# Lưu kết quả vào file analyst_frequency.txt
with open("analyst_frequency.txt", "w") as file:
    for word, count in word_counts.items():
        file.write(f"{word}: {count}\n")
