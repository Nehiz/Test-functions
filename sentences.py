"""A Python program named sentences.py that generates simple English sentences

"""
import random
past = "past"
present = "present"
future = "future"
def main():
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, past)} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, present)} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, future)} {get_adjective()} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, past)} {get_adjective()} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, present)} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, future)} {get_preposition()} {get_prepositional_phrase()} {get_second_prepositional_phrase()}.")

def get_determiner(quantity):

    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman" ]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun
    
def get_verb(quantity, tense):

    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
       verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition from the list of preposition
    given below."""
    prepositions = ["above", "across", "against", "along", "among", 
                    "around","at", "before", "behind", "below", "beneath", 
                    "beside", "between", "by", "down", "into", "near", 
                    "of", "off", "on", "to", "toward", "under", "upon", "within"
                    "about", "after", "in", "without", "towards", "by", "next to", 
                    "beside", "onto", "from", "till", "until", "past", "before"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase():
    """Return a randomly chosen preposition_phrase from the list of preposition_phrase
    given below."""
    prepositional_phrases = ["across the road", "to the door", "behind the door", " under the table", 
                             "off the road", "before the", "at the park", "on time", 
                             "within the house", "beautiful woman", "4 years ago", "live in the", "is laughing"]
    prepositional_phrase = random.choice(prepositional_phrases)
    return prepositional_phrase


def get_second_prepositional_phrase():
    """Return another randomly chosen preposition_phrase from the list of preposition_phrase
    given below."""
    second_propositional_phrases = ["at the end", "on top the mountain", "by the mountain side", "with grace", "over the rainbow",
                                   "out of trouble", "out of stock", "out of ideas", "for safekeeping", "for nothing", "for dinner",
                                    "for a while", "for a good course", "with the aid of", "with respect to", "with an eye to"]
    second_propositional_phrase = random.choice(second_propositional_phrases)
    return second_propositional_phrase

def get_adjective():
    """Return a randomly chosen adjective from the list of adjectives
    given below."""
    adjectives = ["fat", "big", "elegant", "happy", "attractive", "colourful", "short", "tall", "skinny", "beautiful", "gorgeous", "attractive"]
    adjective = random.choice(adjectives)
    return adjective

if __name__ == "__main__":
    main()

