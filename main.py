import jieba
import re
import gensim
import os

#获取指定路径的文件的内容
def gain_content(path):
    string = ''
    file = open(path, 'r', encoding='UTF-8')
    line = file.readline()
    while line:
        string = string+line
        line = file.readline()
    file.close()
    return string

#将文本的标点符号和转义字符过滤掉
def filter(string):
    rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]") #仅保留字母，数字和汉字
    string = rule.sub("", string)
    return string

#对过滤后的文本进行jieba分词
def divide(string):
    result = jieba.lcut(string)
    return result

#对jieba分词后的文本进行余弦相似度计算，从而得到文本相似度
def calc_sim(text1, text2):
    texts = [text1, text2] #建立【分词列表集】
    dictionary = gensim.corpora.Dictionary(texts) #基于【分词列表集】建立【词典】
    corpus = [dictionary.doc2bow(text) for text in texts] #基于【词典】，将【分词列表集】转换为【稀疏向量集】，即【语料库】
    feature_count = len(dictionary) #提取词典特征数
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, feature_count)
    test_corpus1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus1][1]
    return cosine_sim

#得到文本相似度并将其写入txt文件
def main_test():
    path1 = input("论文原文的文件的绝对路径：")
    path2 = input("抄袭版论文的文件的绝对路径：")
    save_path = input("输出的答案文件的绝对路径：")
    if not os.path.exists(path1):
        print("论文原文文件为空")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件为空")
        exit()
    str1 = gain_content(path1)
    str2 = gain_content(path2)
    str_1 = filter(str1)
    str_2 = filter(str2)
    text1 = divide(str_1)
    text2 = divide(str_2)
    similarity = calc_sim(text1, text2)
    result = round(similarity.item(), 2) #使用item()语句将similarity转换为浮点型，再用round()语句保留两位小数
    print("文本相似度：%.2f" % result)
    #将文本相似度结果写入txt文件
    file = open(save_path,'w', encoding ='UTF-8')
    file.write("文本相似度：%.2f" % result)
    file.close()
    return result

if __name__ == '__main__':
    main_test()












