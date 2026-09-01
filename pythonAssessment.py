from collections import Counter
import re

def count_specific_word(text, word):

    if not text or not word:
        return 0 

    text_lower = text.lower()
    word_lower = word.lower()

    words = re.findall(r'\b[a-z0-9\']+\b', text_lower)

    count = words.count(word_lower)

    print(f"The word '{word}' appears {count} times in the given text.")
    return count 


def identify_most_common_word(text):
    if not text or not text.strip():
        print('The input text is empty. Please provide a valid text.')
        return None

    words = re.findall(r'[a-z0-9\']+', text.lower())
    if not words:
        print('No valid words found in the text.')
        return None
    
    word_counts = Counter(words)

    most_common = word_counts.most_common(1)[0][0]

    print(f"The most common word in the given text is: '{most_common}'")
    return most_common


def calculate_average_word_length(text):
    if not text or not text.strip():
        print('Average word length: 0.0')
        return 0.0

    words = re.findall(r'[a-zA-Z0-9\']+', text)

    if not words:
        print('Average word length: 0.0')
        return 0.0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)

    print(f'Average word length: {average_length:.2f}')
    return average_length

def count_paragraphs(text):
    if not text:
        print('Number of paragraphs: 1')
        return 1

    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]

    count = len(paragraphs)

    if count == 0:
        count = 1

    print(f"Number of paragraphs: {count}")
    return count


def count_sentences(text):
    if not text or not text.strip():
        print("Sentence: analysis 1")
        return 1

    abbreviations = r'\b(Mr|Mrs|Ms|Dr|Prof|Sr|Jr|Inc|Ltd|Corp|Co|etc|vs|Fig|Dept|Approx|Misc)\.'
    
    protected = re.sub(abbreviations, r'\1<DOT>', text)
    
    sentences = re.split(r'[.!?]+(?:\s+|$)', protected)
    sentences = [s for s in sentences if s.strip()]

    count = len(sentences)
    count = count if count > 0 else 1
    
    print(f"sentence: analysis {count}") 
    return count
 


if __name__ == '__main__':
    print(" NEWS ARTICLE TEXT ANALYSIS")
    filename = "ACME Inc. Unveils Revolutionary Apple Pie Machine,.txt"

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            article_text = file.read()
        print(f"\n Successfully loaded: {filename}")
    except FileNotFoundError:
        print(f"\n Error: File '{filename}' not found!")
        print("Please make sure the file is in the current directory.")
        print(f"Current directory: {__import__('os').getcwd()}")
        exit(1)
    
    while True:
        print(" TEXT ANALYSIS MENU")
        
        print("1. Count specific word")
        print("2. Find most common word")
        print("3. Calculate average word length")
        print("4. Count paragraphs")
        print("5. Count sentences")
        print("6. Run all analyses")
        print("0. Exit")
        
        
        choice = input("Enter your choice (0-6): ").strip()
        

        if choice == '0':
            print("\n Goodbye!")
            break
        elif choice == '1':
            word = input("Enter word to count: ").strip()
            if word:
                count_specific_word(article_text, word)
            else:
                print(" Please enter a valid word.")
        elif choice == '2':
            identify_most_common_word(article_text)
        elif choice == '3':
            calculate_average_word_length(article_text)
        elif choice == '4':
            count_paragraphs(article_text)
        elif choice == '5':
            count_sentences(article_text)
        elif choice == '6':
            print(" COMPLETE ANALYSIS")
            
            analyses = [
                ("Specific Word Count ('apple')", lambda: count_specific_word(article_text, "apple")),
                ("Most Common Word", lambda: identify_most_common_word(article_text)),
                ("Average Word Length", lambda: calculate_average_word_length(article_text)),
                ("Paragraph Count", lambda: count_paragraphs(article_text)),
                ("Sentence Count", lambda: count_sentences(article_text))
            ]
            
            for name, func in analyses:
                print(f"\n {name}:")
                func()
            

        else:
            print(" Invalid choice. Please enter a number between 0 and 6.")
    
    print(" PROGRAM COMPLETE")





    
