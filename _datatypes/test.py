# Using the letters ['a', 'b', 'c', 'a']:

# Create a list named letters_list that keeps all items in order.
# Create a tuple named letters_tuple with the same items in order.
# Create a set named letters_set from the same items.
# Goal: The set should contain each letter only once.

source_letters = ['a', 'b', 'c', 'a']

letters_list = list(source_letters)
# print(f"{letter_list}")
letters_tuple = tuple(source_letters)
letters_set = set(source_letters)

assert isinstance(letters_list, list), 'letters_list should be a list.'
assert isinstance(letters_tuple, tuple), 'letters_tuple should be a tuple.'
assert isinstance(letters_set, set), 'letters_set should be a set.'

assert letters_list == ['a', 'b', 'c', 'a'], 'List should preserve duplicates and order.'
assert letters_tuple == ('a', 'b', 'c', 'a'), 'Tuple should preserve duplicates and order.'
assert letters_set == {'a', 'b', 'c'}, 'Set should contain unique letters only.'
print('✅ Exercise 1 looks good!')