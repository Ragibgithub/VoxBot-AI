import wikipedia
import sys

def wiki(text):
    text = text.lower()
    a = "search on wikipedia"
    b = "find information about on wikipedia"
    c = "look up on wikipedia"
    d = "what is on wikipedia"
    e = "tell me about"
    f = "who is "
    g = "what is "
    h = "information about"

    if a in text:
        text = text.replace(a, "")
    if b in text:
        text = text.replace(b, "")
    if c in text:
        text = text.replace(c, "")
    if d in text:
        text = text.replace(d, "")
    if e in text:
        text = text.replace(e, "")
    if f in text:
        text = text.replace(f, "")
    if g in text:
        text = text.replace(g, "")
    if h in text:
        text = text.replace(h, "")

    text = text.strip()
    print(text)
    try:
        summary = wikipedia.summary(text, sentences=2)
    except wikipedia.exceptions.PageError:
        summary = f"Sorry, I couldn't find any information about the topic {text} on Wikipedia."
    return text,summary


