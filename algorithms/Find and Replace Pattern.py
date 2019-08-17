class Solution:
    history = set()
    usedLetters = set()
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        copy = words.copy()
        result = list()
        for counter, word in enumerate(copy):
            if len(word) != len(pattern):
                continue
            self.history = set()
            self.usedLetters = set()
            for pos, char in enumerate(pattern):
                if pos not in self.history:
                    word = self.swap(word[pos],word, char,pos)
            if word == pattern:
                result.append(words[counter])
        return result
    
    def swap(self, find: str, word:str, pattern: str,start:int) -> str:
        if pattern in self.usedLetters:
            return word
        result = word[:start]
        for c,i in enumerate(word[start:]):
            if i == find and (c+start) not in self.history:
                self.history.add(c+start)
                result += pattern
            else:
                result += i
        self.usedLetters.add(pattern)
        return result
                
                
                
        