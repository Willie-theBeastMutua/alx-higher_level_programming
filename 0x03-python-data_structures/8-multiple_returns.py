#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len < 1:
        return None
    else:
        tuple_len = (sent_len,)
        tuple_ch = (sentence[0],)
        tuple_len += tuple_ch
    return tuple_len

