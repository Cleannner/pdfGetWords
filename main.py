import pdfplumber
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.data import find


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def clean_text(text):
    # 去掉非字母字符，只保留单词
    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)
    # 转小写，分割为单词列表
    words = cleaned_text.lower().split()
    return words


def get_word_frequencies(words):
    # 统计每个单词的出现次数
    word_count = Counter(words)
    return word_count


# 检查是否已下载 stopwords
def ensure_stopwords_downloaded():
    try:
        find('corpora/stopwords')
    except LookupError:
        print("Stopwords not found. Downloading...")
        nltk.download('stopwords')

# 确保停用词已下载
ensure_stopwords_downloaded()
# 使用停用词
stop_words = set(stopwords.words("english"))

def filter_stopwords(word_count):
    filtered_words = {word: count for word, count in word_count.items() if word not in stop_words}
    return filtered_words


