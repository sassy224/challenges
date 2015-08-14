"""
https://codefights.com/challenge/tCQbdyJMzENW9z4b9
Morse code is a method of transmitting text information as a series of . and - We need a function that given some text returns its representation in morse code. 
Use the following guide:
    A     .-
    B     -...
    C     -.-.
    D     -..
    E     .
    F     ..-.
    G     --.
    H     ....
    I     ..
    J     .---
    K     -.-
    L     .-..
    M     --
    N     -.
    O     ---
    P     .--.
    Q     --.-
    R     .-.
    S     ...
    T     -
    U     ..-
    V     ...-
    W     .--
    X     -..-
    Y     -.--
    Z     --..

Separate each character of the result with a whitespace and replace each original whitespace with two whitespaces (to distinguish it from the spaces between morse characters)

input="ana"
output=".- -. .- "

input="ana y yo"
output=".- -. .-   -.--   -.-- --- "
"""

import re
def morse(text):    

    codes = [
        (r"\s", "  "),
        (r"A", ".- "),
        (r"B", "-... "),
        (r"C", "-.-. "),
        (r"D", "-.. "),
        (r"E", ". "),
        (r"F", "..-. "),
        (r"G", "--. "),
        (r"H", ".... "),
        (r"I", ".. "),
        (r"J", ".--- "),
        (r"K", "-.- "),
        (r"L", ".-.. "),
        (r"M", "-- "),
        (r"N", "-. "),
        (r"O", "--- "),
        (r"P", ".--. "),
        (r"Q", "--.- "),
        (r"R", ".-. "),
        (r"S", "... "),
        (r"T", "- "),
        (r"U", "..- "),
        (r"V", "...- "),
        (r"W", ".-- "),
        (r"X", "-..- "),
        (r"Y", "-.-- "),
        (r"Z", "--.. ")
    ]

    for code in codes:
        regex = re.compile(code[0], re.IGNORECASE)
        text = regex.sub(code[1], text )
    return text

print morse("ana")
print morse("ana y yo")
