class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                      "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                      "..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            morse = ""
            for char in word:
                morse += morse_code[ord(char) - ord('a')]
            transformations.add(morse)
        
        return len(transformations)
