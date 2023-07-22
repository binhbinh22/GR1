import pandas as pd

# Đường dẫn đến file CSV
csv_file_path = "tin_tuc.csv"

data_frame = pd.read_csv(csv_file_path)

titles = data_frame["title"].tolist()

# Từ khóa liên quan đến giá hàng hoá nông sản gạo
keywords = ["giá","gạo", "giảm","tăng","thị trường", "nông sản", "xuất khẩu"]

# Phân tích ngữ cảnh
def analyze_context(text, keywords):
    context_dict = {}
    for keyword in keywords:
        context_dict[keyword] = []

    for sentence in text: # duyệt từng câu 
        words = sentence.split() # tách câu thành các từ riêng lẻ
        for i, word in enumerate(words):
            if word in keywords:
                context = " ".join(words[max(0, i-5):i] + words[i+1:min(i+6, len(words))])
                context_dict[word].append(context)

    return context_dict

# Phân tích ngữ cảnh trong cột "title"
title_contexts = analyze_context(titles, keywords)

# Lưu kết quả vào file analyst_context.txt
with open("analyst_context.txt", "w") as file:
    for keyword, contexts in title_contexts.items():
        file.write(f"Từ khóa: {keyword}\n")
        file.write("Các ngữ cảnh:\n")
        for context in contexts:
            file.write(f"{context}\n")
        file.write("\n")
