import pandas as pd

def xoá_cột(file_gốc, cột_xoá, file_mới):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_gốc)

    # Xoá cột
    df = df.drop(columns=[cột_xoá])

    # Ghi dữ liệu đã chỉnh sửa vào file mới
    df.to_csv(file_mới, index=False)

    print("Đã xoá cột thành công.")

# Sử dụng ví dụ
file_gốc = "baotintuc_nongsan.csv"
cột_xoá = "web-scraper-start-url"
file_mới = "baotintuc_nongsan.csv"

xoá_cột(file_gốc, cột_xoá, file_mới)
