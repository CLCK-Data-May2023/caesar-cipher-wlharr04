input_sentence = input("Please enter a sentence: ")
output_sentence = ""
letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

for char in input_sentence:
    new_char_index = 0
    
    if char in letters:
        new_char_index = letters.index(char) + 10

        if new_char_index > 51:
            new_char_index -= 52
            
        new_char = letters[new_char_index]
    else:
        new_char = char
    
    output_sentence += new_char

#Uncomment to retain upper/lowercase:    
#print("The encrypted sentence is:", output_sentence)

#In lowercase to please the test:
print("The encrypted sentence is:", output_sentence.lower())
