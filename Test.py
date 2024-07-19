import difflib

def highlight_differences(reference, test):
    # Split sentences into words
    reference_words = reference.split()
    test_words = test.split()
    
    # Use difflib to find differences
    diff = difflib.ndiff(reference_words, test_words)
    
    # Highlight differences
    differences = []
    for word in diff:
        if word.startswith('- '):
            differences.append(f"Reference missing: {word[2:]}")
        elif word.startswith('+ '):
            differences.append(f"Extra in test: {word[2:]}")
        elif word.startswith('? '):
            pass  # This line shows markers for different characters, we can ignore it

    return differences

def calculate_errors(reference, test):
    reference_words = reference.split()
    test_words = test.split()
    
    matcher = difflib.SequenceMatcher(None, reference_words, test_words)
    errors = 0
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            errors += max(i2 - i1, j2 - j1)
    
    return errors

def correct_sentence(reference, test):
    reference_words = reference.split()
    test_words = test.split()
    
    matcher = difflib.SequenceMatcher(None, reference_words, test_words)
    corrected_sentence = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            corrected_sentence.extend(test_words[j1:j2])
        elif tag == 'replace':
            corrected_sentence.extend(reference_words[i1:i2])
        elif tag == 'insert':
            corrected_sentence.extend(reference_words[i1:i2])
        elif tag == 'delete':
            continue
    
    return ' '.join(corrected_sentence)

# Reference sentence
reference_sentence = """london the capital city of the united kingdom is a vibrant metropolis rich in history and culture Known as the square mile the city of london is the historic core where the romans first established londinium today it's a major business and financial center housing the Bank of England the royal exchange and the london stock exchange despite its modern skyscrapers like the gherkin and the walkie talkie london retains its historical charm with landmarks such as tower of london the city's boundaries have remained nearly unchanged since medieval times making it a unique blend of ancient and contemporary with a small resident population but a bustling daytime workforce the city is always alive with activity reflecting its status as one of the world's leading financial hubs."""

# Test sentence
test_sentence = """london the capital city of the united kingdom is a fire metabolic rate in history and culture know as the square mile the city of london is the historical where the romans first established london you today it's a major business and financial center hosting the bank of england the royal exchange and london stock exchange despite his mother and sky characters like the hurricane and the walking distance from tower of london the city missouri weather"""

# Check differences
differences = highlight_differences(reference_sentence, test_sentence)

# Print differences
for diff in differences:
    print(diff)

# Calculate errors
errors = calculate_errors(reference_sentence, test_sentence)
print(f"Number of errors: {errors}")

# Correct the test sentence
corrected_sentence = correct_sentence(reference_sentence, test_sentence)
print("Corrected sentence:")
print(corrected_sentence)
