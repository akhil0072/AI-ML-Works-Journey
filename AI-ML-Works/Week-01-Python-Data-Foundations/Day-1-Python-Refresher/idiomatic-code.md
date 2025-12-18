Idiomatic Code
"Idiomatic Python" or "Pythonic" code adheres to the conventions and best practices preferred by experienced Python programmers, emphasizing readability and efficiency. Adopting an idiomatic style makes your code more natural and intuitive to other Python developers. 
Key idiomatic practices include:
The Zen of Python: The guiding principles of Python development, accessible by running import this in a Python interpreter. Principles include "Beautiful is better than ugly" and "Readability counts".
Following PEP 8: Adhering to the official style guide for Python code, which covers naming conventions, whitespace usage (e.g., using 4 spaces for indentation), and line length.
Using Built-ins Effectively: Leveraging Python's extensive standard library and built-in functions (like enumerate(), zip(), min(), max(), and sum()) instead of manually implementing the logic.
List Comprehensions: Using concise syntax for creating lists from other iterables, which is generally more readable than traditional for loops for this purpose.
Context Managers (with statement): Using the with statement for resource management (like file handling or locks) to ensure resources are properly released, even if errors occur.
Truthiness: Using if somelist: or if not somelist: to check for empty or non-empty containers, rather than checking the length. 

#normal code vs idiomatic code flow

1. Normal code

# Normal Python (less idiomatic)
def count_words_normal(word_list):
    # Initialize an empty dictionary to store counts
    word_counts = {}
    
    # Iterate through the list using a manual for loop
    for i in range(len(word_list)):
        word = word_list[i]
        # Check if the word is already in the dictionary
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
            
    return word_counts

# Example usage
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"Normal way: {count_words_normal(data)}")



2. Idiomatic code

from collection import Counter
 
def count_words_idiomatic(word_list):
    return Counter(word_list)

# Example usage
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"Idiomatic way: {count_words_idiomatic(data)}")
