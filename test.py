import pdfplumber
import re


def extract_and_filter_text(pdf_path, keyword="Directions"):
    """
    从PDF中提取文本，并过滤掉指定关键词后的部分内容。
    :param pdf_path: PDF文件路径
    :param keyword: 要过滤的关键词
    :return: 过滤后的文本
    """
    filtered_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # 提取页面文本
            text = page.extract_text()

            # 检查是否包含关键词
            if keyword in text:
                # 分割文本，保留关键词前的内容
                text = re.split(f"{keyword}.*", text, flags=re.DOTALL)[0]

            # 添加到结果文本中
            filtered_text += text + "\n"

    return filtered_text


# 调用函数
pdf_path = "resource/2024年6月英语六级真题(第3套).pdf"
filtered_text = extract_and_filter_text(pdf_path)

# 保存结果到新的文件
with open("filtered_text.txt", "w", encoding="utf-8") as file:
    file.write(filtered_text)


print(filtered_text.txt)
