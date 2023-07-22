import pandas as pd

# Đường dẫn đến file CSV
input_csv_file = "baotintuc_nongsan.csv"
output_csv_file = "point_title.csv"

data_frame = pd.read_csv(input_csv_file)

# Trích xuất cột "title", "title-href", và "time"
titles = data_frame["title"].tolist()
title_hrefs = data_frame["title-href"].tolist()
times = data_frame["time"].tolist()

# Từ khóa
keywords = ["giá", "gạo", "giảm", "tăng", "Thị trường", "nông sản", "xuất khẩu","nông nghiệp","phát triển","lúa","Xuất khẩu"]

# Công thức tính điểm
def calculate_influence_score(text, keywords):
    score = 0
    for keyword in keywords:
        score += text.count(keyword)
    return score

# Tính mức độ ảnh hưởng của tiêu đề
title_scores = {}
for title in titles:
    score = calculate_influence_score(title, keywords)
    title_scores[title] = score

# Tạo DataFrame mới từ kết quả
output_data_frame = pd.DataFrame({
    "title": list(title_scores.keys()),
    "point": list(title_scores.values()),
    "title-href": title_hrefs,
    "time": times
})

#sắp xếp điểm từ cao đến thấp
output_data_frame = output_data_frame.sort_values(by="point", ascending=False)

# Lưu kết quả vào file CSV
output_data_frame.to_csv(output_csv_file, index=False)
