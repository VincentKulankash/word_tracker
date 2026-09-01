import pythonAssessment

def test_count_specific_word():
    print('Testing the count of a specific word in a given text.')
    print('\n Test 1: basic test with sentence')
    text = 'The quick brown fox jumps over the lazy dog'
    result = pythonAssessment.count_specific_word(text, 'The')
    print(f'Expected: 2, Got: {result}')
    assert result == 2, 'Test 1 failed'

    print('\n Test 2: case insensitive test')
    text = 'The quick brown fox jumps over the lazy dog'
    result = pythonAssessment.count_specific_word(text, 'the')
    print(f'Expected: 2, Got: {result}')
    assert result == 2, 'Test 2 failed'

    print('\n Test 3: test with punctuation')
    text = 'The quick brown fox jumps over the lazy dog. The dog barked.'
    result = pythonAssessment.count_specific_word(text, 'dog')
    print(f'Expected: 2, Got: {result}')
    assert result == 2, 'Test 3 failed'

    print("\n Test 4: Word not found")
    text = "Hello world! This is a test."
    result = pythonAssessment.count_specific_word(text, "python")
    print(f"  Expected: 0, Got: {result}")
    assert result == 0, "Test 4 failed!"

    print("\n Test 5: Empty text")
    result = pythonAssessment.count_specific_word("", "hello")
    print(f"  Expected: 0, Got: {result}")
    assert result == 0, "Test 5 failed!"

    print("\n Test 6: Empty word")
    result = pythonAssessment.count_specific_word("Hello world", "")
    print(f"  Expected: 0, Got: {result}")
    assert result == 0, "Test 6 failed!"

    print('\n ALL TESTS PASSED!\n')



def test_identify_most_common_word():
    print("TESTING: identify_most_common_word")

    print("\n Test 1: Basic case")
    text = "The quick brown fox jumps over the lazy dog"
    result = pythonAssessment.identify_most_common_word(text)
    print(f"  Expected: 'the', Got: '{result}'")
    assert result == 'the', "Test 1 failed!"

    print("\n Test 2: Multiple words with same frequency")
    text = "apple banana apple banana cherry"
    result = pythonAssessment.identify_most_common_word(text)
    print(f"  Expected: 'apple', Got: '{result}'")
    assert result == 'apple', "Test 2 failed!"

    print("\n Test 3: With punctuation")
    text = "Hello, world! Hello everyone. Hello world."
    result = pythonAssessment.identify_most_common_word(text)
    print(f"  Expected: 'hello', Got: '{result}'")
    assert result == 'hello', "Test 3 failed!"

    print("\n Test 4: Empty string")
    result = pythonAssessment.identify_most_common_word("")
    print(f"  Expected: None, Got: {result}")
    assert result is None, "Test 4 failed!"

    print("\n Test 5: String with spaces only")
    result = pythonAssessment.identify_most_common_word("   ")
    print(f"  Expected: None, Got: {result}")
    assert result is None, "Test 5 failed!"

    print("\n Test 6: Special characters only")
    result = pythonAssessment.identify_most_common_word("!@#$%^&*")
    print(f"  Expected: None, Got: {result}")
    assert result is None, "Test 6 failed!"

    print('\n ALL TESTS PASSED!\n')


def test_calculate_average_word_length():
    print('Testing the average word length in a given text.')

    print('\n Test 1: Basic test with sentence')
    text = 'The quick brown fox jumps over the lazy dog'
    result = pythonAssessment.calculate_average_word_length(text)
    print(f'Expected: 3.89, Got: {result:.2f}')
    assert round(result, 2) == 3.89, 'Test 1 failed!'

    print("\n Test 2: With punctuation")
    text = "Hello, world! This is a test."
    result = pythonAssessment.calculate_average_word_length(text)
    print(f"  Expected: 3.50, Got: {result:.2f}")
    assert round(result, 2) == 3.50, "Test 2 failed!"

    print("\n Test 3: With numbers")
    text = "Python 3.9 is great"
    result = pythonAssessment.calculate_average_word_length(text)
    print(f"  Expected: 3.00, Got: {result:.2f}")
    assert round(result, 2) == 3.00, "Test 3 failed!"

    print("\n Test 4: Special characters only")
    text = "!@#$%^&*()"
    result = pythonAssessment.calculate_average_word_length(text)
    print(f"  Expected: 0.00, Got: {result:.2f}")
    assert round(result, 2) == 0.00, "Test 4 failed!"

    print("\n Test 5: Empty string")
    result = pythonAssessment.calculate_average_word_length("")
    print(f"  Expected: 0.00, Got: {result:.2f}")
    assert round(result, 2) == 0.00, "Test 5 failed!"

    print("\n Test 6: String with spaces only")
    result = pythonAssessment.calculate_average_word_length("   ")
    print(f"  Expected: 0.00, Got: {result:.2f}")
    assert round(result, 2) == 0.00, "Test 6 failed!"

    print('\n ALL TESTS PASSED!\n')

def test_count_paragraphs():
    print("TESTING: count_paragraphs")

    print("\n Test 1: Single paragraph")
    text = "This is a single paragraph."
    result = pythonAssessment.count_paragraphs(text)
    print(f"  Expected: 1, Got: {result}")
    assert result == 1, "Test 1 failed!"

    print("\n Test 2: Two paragraphs")
    text = "First paragraph.\n\nSecond paragraph."
    result = pythonAssessment.count_paragraphs(text)
    print(f"  Expected: 2, Got: {result}")
    assert result == 2, "Test 2 failed!"

    print("\n Test 3: Three paragraphs")
    text = "First.\n\nSecond.\n\nThird."
    result = pythonAssessment.count_paragraphs(text)
    print(f"  Expected: 3, Got: {result}")
    assert result == 3, "Test 3 failed!"

    print("\n Test 4: With whitespace in empty lines")
    text = "First paragraph.\n\n   \n\nSecond paragraph."
    result = pythonAssessment.count_paragraphs(text)
    print(f"  Expected: 2, Got: {result}")
    assert result == 2, "Test 4 failed!"

    print("\n Test 5: Empty string")
    result = pythonAssessment.count_paragraphs("")
    print(f"  Expected: 1, Got: {result}")
    assert result == 1, "Test 5 failed!"

    print("\n Test 6: String with only whitespace")
    result = pythonAssessment.count_paragraphs("   \n   \n   ")
    print(f"  Expected: 1, Got: {result}")
    assert result == 1, "Test 6 failed!"

    print('\n All tests passed!\n')


def test_count_sentences():
    print("TESTING: count_sentences")

    print("\n Test 1: Basic sentences")
    text = "Hello world. How are you? I'm fine!"
    result = pythonAssessment.count_sentences(text)
    print(f"  Expected: 3, Got: {result}")
    assert result == 3, "Test 1 failed!"

    print("\n Test 2: Single sentence")
    text = "This is one sentence."
    result = pythonAssessment.count_sentences(text)
    print(f"  Expected: 1, Got: {result}")
    assert result == 1, "Test 2 failed!"

    print("\n Test 3: Question marks")
    text = "Is this a question? Yes it is. Are you sure? Absolutely."
    result = pythonAssessment.count_sentences(text)
    print(f"  Expected: 4, Got: {result}")
    assert result == 4, "Test 3 failed!"

    print("\n Test 4: Exclamation marks")
    text = "Wow! Amazing! Incredible!"
    result = pythonAssessment.count_sentences(text)
    print(f"  Expected: 3, Got: {result}")
    assert result == 3, "Test 4 failed!"

    print("\n Test 5: Abbreviations")
    text = "ACME Inc. is a company. Dr. Smith works there."
    result = pythonAssessment.count_sentences(text)
    print(f"  Expected: 2, Got: {result}")
    assert result == 2, "Test 5 failed!"

    print("\n Test 6: Empty string")
    result = pythonAssessment.count_sentences("")
    print(f"  Expected: 1, Got: {result}")
    assert result == 1, "Test 6 failed!"

    print('\n ALL TESTS PASSED!\n')



if __name__ == '__main__':
    test_calculate_average_word_length()
    test_identify_most_common_word()
    test_count_specific_word()
    test_count_paragraphs()
    test_count_sentences()
    







     

     

