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
        with open(filename,newline="",encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader:
                cleanned_comments = clean_text(row['Komentar'])
                data.append({
                    "idKomentar": row["idKomentar"],
                    "idBerita": row["idBerita"],
                    "komentar": " ".join(cleanned_comments),
                    "rating": row["Rating"]
                })
        
    except FileNotFoundError:
        return f"Error: File '{filename}' tidak ditemukan."                    
    return data

def read_news(filename):
    data=[]
    try:
        with open(filename,newline="",encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader:
                cleanned_content = clean_text(row['Content'])
                data.append({
                    "idBerita": row["idBerita"],
                    "headline": row["Headline"],
                    "content": " ".join(cleanned_content),
                })
    except FileNotFoundError:
        return f"Error: File '{filename}' tidak ditemukan."  
    return data

        
    