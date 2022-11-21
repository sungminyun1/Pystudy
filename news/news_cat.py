import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

def get_contents(file_list):
    Y_class = []
    X_text = []
    class_dict = {
        1: '0', 2: '0', 3: '0', 4: '0', 5: '1', 6: '1', 7: '1', 8: '1',
    }

    for file_name in file_list:
        try:
            f = open(file_name,'r',encoding='cp949')
            category = int(file_name.split(os.sep)[1].split('_')[0])
            Y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text,Y_class


def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleanad_words = [get_cleaned_text(word) for words in text for word in words]

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i,v in enumerate(set(cleanad_words)):
        corpus_dict[v] = i
    return corpus_dict

def get_cleaned_text(text):
    import re
    text = re.sub('\W+','',text.lower())
    return text

if __name__ == '__main__':
    dir_name = 'news_data'
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name,file_name) for file_name in file_list]

    X_text , y_class = get_contents(file_list)

    corpus = get_corpus_dict(X_text)

    print(corpus)
    