def anagrams(word1 :str, word2: str) -> bool:
    word1 = str(word1)
    word2 = str(word2)
    anagrams = True
    for i in word1:
        if not i in word2:
            anagrams = False
            break
    if anagrams:
        for i in word2:
            if not i in word1:
                anagrams = False
                break
    return anagrams

print(anagrams("team", "tame"))