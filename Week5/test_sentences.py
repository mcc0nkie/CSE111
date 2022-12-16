import pytest
from sentences import get_verb, get_determiner, get_noun


def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_plural_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_singular_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"]

    for i in range(20):
        past = get_verb(1, '1')
        present_sing = get_verb(1, '2')
        present_plural = get_verb(2, '2')
        future = get_verb(1, '3')

        assert past in past_verbs
        assert present_sing in present_singular_verbs
        assert present_plural in present_plural_verbs
        assert future in future_verbs



def test_get_determiner():
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    for i in range(20):
        word = get_noun(1)
        assert word in singular_nouns
    
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for i in range(20):
        word = get_noun(2)
        assert word in plural_nouns

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])