"""
Challenge 3: Sort Words
"""

def sort_words(_string):
    """
    sort words in string while maintaing case.
    """
    return sorted(_string.split(), key=lambda x: x.lower())

print(sort_words('this is My String you understand'))