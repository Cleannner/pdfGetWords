import spacy
import re

# 加载 Spacy 英文模型
nlp = spacy.load("en_core_web_sm")


def spacy_word_tokenize(text):
    """
    使用 Spacy 分词，清理并处理输入文本。
    :param text: 原始未分词文本
    :return: 分词后的文本
    """
    # 修复被连字符和换行符打断的单词
    text = re.sub(r"-\n", "", text)
    # 替换换行符为空格，保持段落连续性
    text = re.sub(r"\n", " ", text)

    # 使用 Spacy 进行分词处理
    doc = nlp(text)

    # 提取分词结果
    tokens = [token.text for token in doc]
    return " ".join(tokens)


# 示例测试
raw_text = """SometimeswebecomeaccustomedtorelyingonourgutsThisservesuswellincertain
situations,butcanhinderusinothersespeciallywhenweindulginginvideogames"""
cleaned_text = spacy_word_tokenize(raw_text)
print(cleaned_text)
