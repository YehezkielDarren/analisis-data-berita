import csv
import string

def clean_text(data):
    text = data.lower().rstrip()
    translator = str.maketrans("","", string.punctuation+string.digits)
    result = text.translate(translator).split()
    return result         

def read_news(filename):
    data = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cleanned_content = clean_text(row['Content'])
                data.append({
                    "idBerita": row["idBerita"],
                    "headline": row["Headline"],
                    "content": cleanned_content,
                })
    except FileNotFoundError:
        return f"Error: File '{filename}' tidak ditemukan."
    return data

def find_top_words(data, n=10):
    word_count = {}
    for entry in data:
        for word in entry['content']:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    # Sort descending to find the top N, then reverse the result for ascending order
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    top_n_ascending = sorted_words[:n]
    return dict(top_n_ascending)