"""
Challenge 2. Palindrome
"""
import re


def is_palindrome(_string: str):
    """
    Determine if _string is palindrome
    """
    str1 = "".join(re.findall(r'[a-z]+', _string.lower()))
    str2 = str1[::-1]
    return str1 == str2

print(is_palindrome('malay.22 alam'))