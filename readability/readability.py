letters, words, sentences = 0, 1, 0


def count_letters(text, letters):
    for c in range(len(text)):
        if text[c].isalpha():
            letters += 1
    return letters


def count_words(text, words):
    for c in range(len(text)):
        if text[c].isspace():
            words += 1
    return words


def count_sentences(text, sentences):
    for c in range(len(text)):
        if text[c] == "!" or text[c] == "?" or text[c] == ".":
            sentences += 1
    return sentences


text = input("Text: ")  # possivelmente necessario usar get_string

letters = count_letters(text, letters)
words = count_words(text, words)
sentences = count_sentences(text, sentences)

index = round(0.0588 * (float(letters) / float(words) * 100) - 0.296 * (float(sentences) / float(words) * 100) - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {int(index)}")

#print(f"Letters: {letters}")
#print(f"Words: {words}")
#print(f"Sentences: {sentences}")