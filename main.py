#open csv file
#extract author keywords and index keywords

import csv
from collections import defaultdict

author_keywords = defaultdict(int)
index_keywords = defaultdict(int)

with open("raw.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        author_kw = row.get("Author Keywords", "").split(";")
        index_kw = row.get("Index Keywords", "").split(";")

        for kw in author_kw:
            kw1 = kw.strip()
            author_keywords[kw1] += 1
        
        for kw in index_kw:
            kw2 = kw.strip()
            index_keywords[kw2] += 1

top_author_keywords = sorted(author_keywords.items(), key=lambda x : x[1], reverse=True)[:15]
top_index_keywords = sorted(index_keywords.items(), key = lambda x : x[1], reverse = True)[:15]
print(top_author_keywords)
print(top_index_keywords)