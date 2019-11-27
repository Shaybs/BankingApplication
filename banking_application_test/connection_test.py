import pytest
from banking_application import banking_application

#No numbers test
def test_anti_vowel_vowels():
    assert anti_vowel.anti_vowel("ooooooooooooooooooooooooooooooooooooooooooooooooo")==''

def test_anti_vowel_novowels():
    assert anti_vowel.anti_vowel("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")=='kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'

def test_anti_vowel_random():
    assert anti_vowel.anti_vowel("aaab")=='b'
