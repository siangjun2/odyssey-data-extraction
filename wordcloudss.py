#import pdf one by one
#read pdf, and convert to freq array
#display as word cloud

import os
from PyPDF2 import PdfReader
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def get_word_frequencies(text):
    # Simple list of common stopwords
    stopwords = {
        "the", "and", "a", "an", "of", "to", "in", "is", "it", "for", "on", "with", "as", "by", "at", "from", "that",
        "this", "be", "are", "was", "were", "or", "but", "not", "which", "can", "has", "have", "had", "will", "would",
        "should", "could", "may", "might", "do", "does", "did", "so", "if", "than", "then", "also", "such", "we", "you", "your", "they", "their", "he", "she", "his", "her", "its", "my", "our", "us", "me", "him", "them", "there", "here", "where", "when", "why", "how", "what", "who", "whom", "which", "whose", "all", "any", "some", "no", "yes", "more", "most", "much"
    }
    words = [word.lower() for word in text.split()]
    filtered_words = [word for word in words if word not in stopwords and word.isalpha()]
    return Counter(filtered_words)

def save_wordcloud(freq, output_path):
    wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_path)
    plt.close()

def main(pdf_folder, clouds_folder):
    os.makedirs(clouds_folder, exist_ok=True)
    all_frequencies = Counter()

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            freq = get_word_frequencies(text)
            all_frequencies += freq

            cloud_path = os.path.join(clouds_folder, f"{os.path.splitext(filename)[0]}_cloud.png")
            save_wordcloud(freq, cloud_path)

    # Save combined word cloud
    combined_cloud_path = os.path.join(clouds_folder, "combined_cloud.png")
    save_wordcloud(all_frequencies, combined_cloud_path)

if __name__ == "__main__":
    pdf_folder = os.path.join(os.path.dirname(__file__), "pdfs")
    clouds_folder = os.path.join(os.path.dirname(__file__), "clouds")
    main(pdf_folder, clouds_folder)