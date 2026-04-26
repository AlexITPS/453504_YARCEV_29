"""
Purpose: Regex operations for text analysis.
LW 4 (Task 2)
Version 1.0
"""

import re

def regex_strip(text: str) -> str:
    """
    Custom implementation of strip() using only regex.
    """
    return re.sub(r'^\s+|\s+$', '', text)

def count_sentences(text: str):
    """Counts declarative (.), interrogative (?), and imperative (!) sentences."""
    dec = len(re.findall(r'[^!?.]+\.', text))
    ques = len(re.findall(r'[^!?.]+\?', text))
    imp = len(re.findall(r'[^!?.]+\!', text))
    return dec, ques, imp

def get_avg_lengths(text: str):
    """Average sentence length (in chars, words only) and average word length."""
    words = re.findall(r'[a-zA-Zа-яА-ЯёЁ0-9]+', text)
    if not words:
        return 0, 0

    avg_word = sum(len(w) for w in words) / len(words)

    sentences = re.split(r'[.!?]+', text)
    sentence_char_counts = []
    
    for s in sentences:
        if re.search(r'[a-zA-Zа-яА-ЯёЁ0-9]', s):
            s_words = re.findall(r'[a-zA-Zа-яА-ЯёЁ0-9]+', s)
            sentence_char_counts.append(sum(len(w) for w in s_words))

    avg_sent = sum(sentence_char_counts) / len(sentence_char_counts) if sentence_char_counts else 0
    return avg_sent, avg_word

def get_smiley_count(text: str):
    """Finds smileys count using regex backreferences for identical brackets."""
    pattern = r'[;:][-]*([\(\)\[\]])\1*'
    return len(re.findall(pattern, text))

def find_lowercase_digit_words(text: str):
    """Finds words containing at least one lowercase letter and one digit."""
    pattern = r'\b(?=[^ ]*[a-zа-яё])(?=[^ ]*\d)[a-zа-яё0-9]+\b'
    return re.findall(pattern, text)

def is_valid_ip(text: str):
    """Checks if a string is a valid IPv4 address using regex."""
    clean_text = regex_strip(text)
    
    octet = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    pattern = f'^{octet}\.{octet}\.{octet}\.{octet}$'
    return bool(re.match(pattern, clean_text))

def count_lowercase_letters(text: str):
    """Count all lowercase letters in the text."""
    return len(re.findall(r'[a-zа-яё]', text))

def find_v_word(text: str):
    """Finds first word with 'v' and its index using re.search."""
    words = re.findall(r'\b\w+\b', text)
    for i, word in enumerate(words, 1):
        if re.search(r'v', word):   #r[vV]
            return word, i
    return None, None

def remove_s_words(text: str):
    """Removes words starting with 's' and cleans result with regex_strip."""
    result = re.sub(r'\bs\w*\b', '', text) # \b[sS]...
    return regex_strip(result)