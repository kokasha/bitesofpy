def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    
    if word1.strip() == word2.strip(): return False
    chr_word1 = [l for l in word1.lower().replace(' ', '')]
    ch_word2 = [l for l in word2.lower().replace(' ', '')]
    try:
      for chr in ch_word2:
         chr_word1.remove(chr)
    except ValueError:
         return False
    if len(chr_word1) != 0: 
      return False
    else:
       return True
