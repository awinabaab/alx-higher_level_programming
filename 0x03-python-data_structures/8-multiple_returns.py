#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    first_char = sentence[0] if sentence_len > 0 else None
    return (sentence_len, first_char)
