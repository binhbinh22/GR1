import pandas as pd
from collections import Counter

csv_file_path = "ketqua.csv"

data_frame = pd.read_csv(csv_file_path)

# Trích xuất cột "entity"
entities = data_frame["entity"].tolist()

# Tính tần suất cụm từ
phrase_counts = Counter(entities)

# Sắp xếp từ 
sorted_phrases = sorted(phrase_counts.items(), key=lambda x: x[1], reverse=True)

# Tạo dataframe mới từ kết quả đã sắp xếp
sorted_data_frame = pd.DataFrame(sorted_phrases, columns=["entity", "count"])

# Lưu kết quả 
# with open("analyst_frequency_entity.txt", "w") as file:
#     for phrase, count in phrase_counts.items():
#         file.write(f"{phrase}: {count}\n")
sorted_data_frame.to_csv("analyst_frequency_entity.txt", index=False)

