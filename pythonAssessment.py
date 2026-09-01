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

    
