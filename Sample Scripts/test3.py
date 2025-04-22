def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

paragraph = "This is a test paragraph with several words."
print("Word count:", count_words(paragraph))
