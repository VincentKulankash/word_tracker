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

if __name__ == '__main__':
    test_count_specific_word()


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

if __name__ == '__main__':
    test_identify_most_common_word()


     

     

