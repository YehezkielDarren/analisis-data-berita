import csv
import string
import pandas as pd
import io

def clean_text(data:str) -> list:
    text = data.lower().rstrip()
    translator = str.maketrans("","", string.punctuation+string.digits)
    result = text.translate(translator).split()
    return result
    
def read_comment(filename):
    data=[]
    try:
        string_data = filename.getvalue().decode("utf-8")
        stringio_obj = io.StringIO(string_data)
        csv_reader = csv.DictReader(stringio_obj)
        for row in csv_reader:
            cleanned_comments = clean_text(row['Komentar'])
            data.append({
                "idKomentar": row["idKomentar"],
                "idBerita": row["idBerita"],
                "komentar": cleanned_comments,
                "rating": row["Rating"]
            })
    except FileNotFoundError:
        return f"Error: File '{filename}' tidak ditemukan."                    
    return data

def read_news(filename):
    data=[]
    try:
        string_data = filename.getvalue().decode("utf-8")
        stringio_obj = io.StringIO(string_data)
        csv_reader = csv.DictReader(stringio_obj)
        for row in csv_reader:
            cleanned_content = clean_text(row['Content'])
            data.append({
                "idBerita": row["idBerita"],
                "headline": row["Headline"],
                "content": cleanned_content
            })
    except FileNotFoundError:
        return f"Error: File '{filename}' tidak ditemukan."  
    return data

# if __name__ == "__main__":
#     # read all datas
#     comment_news = read_comment("./comment_news.csv")
#     news = read_news("./news_data.csv")
    
#     words_dict = dict()
#     words = [x["komentar"] for x in comment_news] + [y["content"] for y in news]
#     # Flatten the list of lists into a single list of words
#     all_words = []
#     for word_list in words:
#         all_words.extend(word_list)
#     # Count word frequency
#     for word in all_words:
#         if word in words_dict:
#             words_dict[word] += 1
#         else:
#             words_dict[word] = 1
#     # Sort the words_dict by frequency in descending order
#     sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
#     df = pd.DataFrame(sorted_words, columns=['word', 'frequency'])
#     print(df.head(10))
        
    