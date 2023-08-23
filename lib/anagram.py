# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = self.sort_word(self.word)

    def sort_word(self,word):
        return ''.join(sorted(word))

    def match(self, anagram_list):
        anagram_matches = []

        for anagram in anagram_list:
            # self.word != anagram.lower() 
            if self.sorted_word == self.sort_word(anagram.lower()):
                anagram_matches.append(anagram)

        return anagram_matches
    
        
    
