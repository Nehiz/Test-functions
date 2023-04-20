from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the singlular noun determiners.

    single_noun_determiners = ["bird", "boy", "car" , "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(10):

        # Call the get_noun function which
        # should return a singular noun.
        noun = get_noun(1)

        # Verify that the noun returned from the get_noun
        # is one of the words in the singular noun determiners list.
        assert noun in single_noun_determiners

    # 2. Test the plural noun determiners.

    plural_noun_determiners = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_noun function which
        # should return a plural noun.
        noun = get_noun(2)

        # Verify that the noun returned from get_noun
        # is one of the words in the plural_noun_determiners list.
        assert noun in  plural_noun_determiners


def test_get_verb():

    # 1. Test the past tense verb determiners.

    past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a past tense verb.
        verbs = get_verb(1, "past")

        # Verify that the verb returned from get_verb
        # is one of the words in the past tense list.
        assert verbs in past

    # 2. Test the present-singular tense verb.
    present = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a present singular verb.
        verbs = get_verb(1, "present")

        # Verify that the verb returned from get_verb
        # is one of the words in the present_singular verb list.
        assert verbs in present

    # 3. Test the present_plural tense verb.
    present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a present plural verb.
        verbs = get_verb(2, "present")

        # Verify that the verb returned from get_verb
        # is one of the words in the present_plural verb list.
        assert verbs in present

    
     # 3. Test the future determiners.

    future = ["will drink", "will eat", "will grow", "will laugh", "will think", 
              "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a future determiner.
        verbs = get_verb(1, "future")

        # Verify that the verb returned from get_verb
        # is one of the words in the future verb list.
        assert verbs in future
 

def test_get_preposition():
    # 1. Test the get_prepositional.

    prepositions = ["above", "across", "against", "along", "among",
                    "around", "at", "before", "behind", "below", "beneath",
                    "beside", "between", "by", "down", "into", "near",
                    "of", "off", "on", "to", "toward", "under", "upon", "within"
                    "about", "after", "in", "without", "towards", "by", "next to",
                    "beside", "onto", "from", "till", "until", "past", "before"]

    # This loop will repeat the statements inside it 39 times.
    for _ in range(39):

        # Call the get_preposition function which
        # should return a preposition.
        preposition = get_preposition()

        # Verify that the preposition returned from the get_preposition
        # is one of the words in the preposition list.
        assert preposition in prepositions

def test_get_preposition_phrase():
    # 1. Test the get_prepositional_phrase.

    prepositional_phrases = ["across the road", "to the door", "behind the door", " under the table",
                    "off the road", "before the", "at the park", "on time",
                             "within the house", "beautiful woman", "4 years ago", "live in the", "is laughing"]
    # This loop will repeat the statements inside it 12 times.
    for _ in range(13):

        # Call the get_preposition_phrase function which
        # should return a preposition_phrase.
        preposition_phrase = get_prepositional_phrase()

        # Verify that the prepositional_phrase returned from the get_prepositional_phrase
        # is one of the words in the preposition list.
        assert preposition_phrase in prepositional_phrases

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
