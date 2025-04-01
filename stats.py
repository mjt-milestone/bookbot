def get_num_words(text):
    """
    This function takes a string and returns the number of words in the string.
    """
    if text:
        words = text.split()
        return len(words)
    else:
        return 0

def count_characters(text):
    """
    This function takes a string and returns a count of each unique alphanumeric character in the string, regardless of capitalization.
    """
    if text:
        # Convert text to lowercase to ignore capitalization
        text = text.lower()
        
        # Initialize a dictionary to store character counts
        char_count = {}
        
        # Iterate over each character in the text
        for char in text:
            if char.isalnum():  # Check if the character is alphanumeric
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        
        return char_count
    else:
        return {}
    
def sort_report(char_count):
    """
    This function takes the dictionary of characters and returns a sorted list of dictionaries.
    """
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():  # Skip non-alphabetical characters
            sorted_list.append({'character': char, 'count': count})
    sorted_list.sort(key=lambda x: x['count'], reverse=True)  # Sort by count in descending order
    return sorted_list