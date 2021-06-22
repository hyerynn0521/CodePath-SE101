class LetterFilter:

    def __init__(self, s):
        self.s = s
        
# Enter your code here. 
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
# class LetterFilter:
#
#   def __init__(self, s):
#       self.s = s
	
    def filter_vowels(self):
        # Enter your code here
        # Return a string
        i = 0
        string = self.s
        while i < len(string):
            if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
                array = string.split(string[i])
                string = ''.join(array)
            else:
                i += 1
        return string

    def filter_consonants(self):
        # Enter your code here
        # Return a string
        i = 0
        string = self.s
        while i < len(string):
            if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
                array = string.split(string[i])
                string = ''.join(array)
            else:
                i += 1
        return string
s = input()



