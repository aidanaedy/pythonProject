import re

pattern = r'ab'
text = 'abc acb'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")

# Pattern: ab
# Text: abc acb
# Matches: ['ab']

################################

pattern = r'.'
text = 'abcdef'

# Pattern: .
# Text: abcdef
# Matches: ['a', 'b', 'c', 'd', 'e', 'f']
#######################

pattern = r'\d'
text = 'FirstWord 1 LastWord'

# Pattern: d
# Text: FirstWord 1 LastWord
# Matches: ['1']

##########################

pattern = r'\D'
text = 'FirstWord 1 LastWord'

# Pattern: D
# Text: FirstWord 1 LastWord
# Matches: ['F', 'i', 'r', 's', 't', 'W', 'o', 'r', 'd', ' ', ' ', 'L' 'a', 's', 't', 'W', 'o', 'r', 'd']

##########################

pattern = r'\w'
text = 'FirstWord 1 LastWord'

# Pattern: w
# Text: FirstWord 1 LastWord
# Matches: ['F', 'i', 'r', 's', 't', 'W', 'o', 'r', 'd', '1', 'L' 'a', 's', 't', 'W', 'o', 'r', 'd']
# \w matches word characters, any character that can be used as a part of a word.

##########################

pattern = r'\s'
text = 'FirstWord 1 LastWord'

# Pattern: s
# Text: FirstWord 1 LastWord
# Matches: [' ', ' ']
# 10. To match just the whitespace characters, the spaces on either side of the digit, change the value of the pattern string to \s

##########################

pattern = r'\w+'
text = 'FirstWord 1 LastWord'

# Pattern: w+
# Text: FirstWord 1 LastWord
# Matches: ['FirstWord', '1',  'LastWord']
#The combination of the word character class (\w) with the plus symbol quantifier (+) will match one or more word characters. 
# To describe that in a different way, you have matched the words in the text, ignoring the spaces between the words.

##########################

pattern = r'[4-6]'
text = '123456789'

# Pattern: r
# Text: 123456789
# Matches: ['4', '5', '6']
# This pattern is a type of character class that you can use to match a range of characters. 
# You specify the range you want to match inside square brackets and separate the start and end of the range with a dash.

##########################

pattern = r'[4-6]'
text = '123456789'

# Pattern: r
# Text: 123456789
# Matches: ['456']
# To produce one match instead of three, replace the value of the pattern string with [4-6]+ and run

##########################

pattern = r'[d-f]+'
text = 'abcdefghi'


# Text: abcdefghi
# Matches: ['def']
# To produce one match instead of three, replace the value of the pattern string with [4-6]+ and run

############################

pattern = r'[a-z0-9]+'
text = 'word!1234?wordandletters'
# You will see three matches.
# This pattern has matched groups of characters separated by an exclamation mark and a question mark.

############################


pattern = r'[^aeuio]+'
text = 'The quick brown fox jumps over the lazy dog.'

# You will see the following:
# Matches: ['Th', 'q', 'ck br', 'wn f', 'x j', 'mps ', 'v', 'r', th, 'l', 'zy', 'd', 'g']  
# This pattern has matched groups that include consonants and spaces in the text, but not the vowels. 
# The caret symbol (^) is used to negate the proceeding right-hand characters.
