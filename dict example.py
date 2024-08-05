# Define the dictionary with a set, a tuple, and a list
my_dict = {
    'set_key': {1, 2, 3, 4},
    'tuple_key': (5, 6, 7, 8),
    'list_key': [9, 10, 11, 12]
}

# Iterate over the dictionary items
for key, value in my_dict.items():
    print(f"Key: {key}")
    print("Values:")
    
    # Check the type of value and print accordingly
    if isinstance(value, set):
        for item in value:
            print(f"  Set item: {item}")
    elif isinstance(value, tuple):
        for item in value:
            print(f"  Tuple item: {item}")
    elif isinstance(value, list):
        for item in value:
            print(f"  List item: {item}")
    print()  # Print a newline for better readability
