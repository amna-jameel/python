# Exercise 9: Word counter (return a dictionary)
# Write count_words(sentence) that returns a dictionary of how many times each word
# appears. Treat The and the as the same word.
# Test: count_words("The cat and the dog and the bird") → {'the': 3, 'cat': 1, 'and': 2, 'dog': 1,
# 'bird': 1}

def count_words(sentence):
    sentence= sentence.lower()
    words= sentence.split()
    words_count={}
    count=0
    for wor in words:
        if wor not in words_count:
            words_count[wor] = 1
        else :
            words_count[wor] =words_count[wor] + 1

    return words_count
words_count = count_words("hi amna how are yopur amna  nhhha hi hi hi ")
print(words_count)
    


