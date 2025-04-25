
def get_num_words(text):
    words = text.split()
    return len(words)

# takes the text from the book as a string and returns the number of times each character appears
def get_character_count(text):
    character_count = {}
    for character in text:
        # convert character to lowercase
        character = character.lower()
        # if the character is in the character_count dictionary, increment its count
        if character in character_count:
            character_count[character] += 1
        # otherwise add it to the dictionary with a count of 1
        else:
            character_count[character] = 1
    # return the character count dictionary
    return character_count

# function that takes the dictionary of characters and their counts and returns a sorted list of dictionaries
# each dictionary should have two key-value pairs: one for the character itself and one for that character's count
# sort the list from greatest to least by the count 
# use .sort() and .isalpha() to skip non-alphabetic characters
# format output to look like: 
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
def sort_character_count(character_count):
    sorted_characters = []
    for character, count in character_count.items():
        if character.isalpha():  # Only include alphabetic characters
            sorted_characters.append({'character': character, 'count': count})
    sorted_characters.sort(key=lambda x: x['count'], reverse=True)
    # Format the output as a list of strings
    sorted_characters = [f"{item['character']}: {item['count']}" for item in sorted_characters]
    # Return the sorted list with each character and its count on a new line
    sorted_characters = "\n".join(sorted_characters)
    return sorted_characters