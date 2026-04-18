import pytest

def find_longest_word(texts):
    result = []
    for text in texts:
        words = text.split()
        longest_word = max(words, key=len)
        result.append(longest_word)
    return result

@pytest.mark.parametrize("texts, expected", [
    (["hello world", "this is a test"], ["hello", "test"]),
    (["python is fun", "i love coding"], ["python", "coding"]),
    (["short", "longer", "longest word"], ["short", "longer", "longest"]),
])
def test_find_longest_word(texts, expected):
    assert find_longest_word(texts) == expected
