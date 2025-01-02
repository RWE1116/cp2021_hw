import streamlit as st

def download_file(file_path, file_label, mime_type, file_name):
    """通用文件下載功能"""
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label=file_label,
                data=file.read(),
                file_name=file_name,
                mime=mime_type
            )
    except FileNotFoundError:
        st.error(f"找不到文件：{file_path}")

# 顯示相關資料下載部分
st.subheader("相關資料下載")

# 下載文件2 (水衝擊實驗)
download_file(r"Y:/a/downloads/實驗2. 水衝擊實驗.pdf", "下載 實驗2. 水衝擊實驗.pdf", "application/pdf", "實驗2. 水衝擊實驗.pdf")
download_file(r"Y:/a/downloads/實驗2. 水衝擊實驗.doc", "下載 實驗2. 水衝擊實驗.doc", "application/msword", "實驗2. 水衝擊實驗.doc")
download_file(r"Y:/a/downloads/實驗2.水衝擊實驗.xls", "下載 實驗2.水衝擊實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗2.水衝擊實驗.xls")

# 下載文件3 (伯努利文氏管實驗)
download_file(r"Y:/a/downloads/實驗3.伯努利文氏管實驗.pdf", "下載 實驗3.伯努利文氏管實驗.pdf", "application/pdf", "實驗3.伯努利文氏管實驗.pdf")
download_file(r"Y:/a/downloads/實驗3.伯努利文氏管實驗.doc", "下載 實驗3.伯努利文氏管實驗.doc", "application/msword", "實驗3.伯努利文氏管實驗.doc")
download_file("Y:/a/downloads/文氏管.STEP", "下載 文氏管.STEP 檔案", "application/step", "文氏管.STEP")

# 下載 第5組 實驗5.溫度與散熱實驗 PDF 檔案
download_file(r"Y:/a/downloads/第5組 實驗5.溫度與散熱實驗.pdf", "下載 第5組 實驗5.溫度與散熱實驗 PDF 檔案", "application/pdf", "第5組 實驗5.溫度與散熱實驗.pdf")

# 下載 第5組 實驗5.溫度與散熱實驗 DOC 檔案
download_file(r"Y:/a/downloads/第5組 實驗5.溫度與散熱實驗.doc", "下載 第5組 實驗5.溫度與散熱實驗 DOC 檔案", "application/msword", "第5組 實驗5.溫度與散熱實驗.doc")

# 下載文件6 (真空抽氣性能實驗)
download_file(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.pdf", "下載 實驗6. 真空抽氣性能實驗.pdf", "application/pdf", "實驗6. 真空抽氣性能實驗.pdf")
download_file(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.doc", "下載 實驗6. 真空抽氣性能實驗.doc", "application/msword", "實驗6. 真空抽氣性能實驗.doc")
download_file("Y:/a/downloads/final.stp", "下載 真空管.stp", "application/stp", "final.stp")
download_file(r"Y:/a/downloads/實驗6.真空抽氣性能實驗.xls", "下載 實驗6.真空抽氣性能實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗6.真空抽氣性能實驗.xls")
download_file(r"Y:/a/downloads/Vacuum Generator Design(1131225)template.xlsx", "下載 Vacuum Generator Design(1131225)template.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Vacuum Generator Design(1131225)template.xlsx")

# 下載 ZIP 文件 (Venturi Geom)
download_file(r"Y:/a/downloads/Venturi_Geom_3d.zip", "下載 Venturi_Geom_3d.zip", "application/zip", "Venturi_Geom_3d.zip")
download_file(r"Y:/a/downloads/Venturi_Geom_2d.zip", "下載 Venturi_Geom_2d.zip", "application/zip", "Venturi_Geom_2d.zip")
download_file(r"Y:/a/downloads/3D(Generator).zip", "下載 3D(Generator).zip", "application/zip", "3D(Generator).zip")