# Programming Assignment-3: Vowels

''' 
	Question: Given a string S of lowercase letters, remove consecutive vowels from S.
		  After removing, the order of the list should be maintained.
'''

# Code 

def is_vow(character): 
    if (character == 'a') or (character == 'e') or (character == 'i') or (character == 'o') or (character == 'u'):
        return True
  
def removeVowels(string): 
    print(string[0], end = "") 
    for i in range(1,len(string)): 
        if ((is_vow(string[i - 1]) != True) or (is_vow(string[i]) != True)): 
              print(string[i], end = "")
input_string = input().strip() 
removeVowels(input_string)
