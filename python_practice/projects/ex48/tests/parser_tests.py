from nose.tools import *
from ex48.parser import *
from ex48.lexicon import *

test = ParserMethods()
def test_Sentence():
    test_true = Sentence(('noun', 'princess'), ('verb', 'kill'), ('noun', 'bear'))
    assert_equal([test_true.subject, test_true.object, test_true.verb],
                ['princess', 'bear', 'kill'])


def test_peek():
    word_list1 = scan('the bear eat the honey')
    assert_equal(test.peek(word_list1), 'stop')

    word_list2 = [('noun', 'bear'), ('verb', 'go'), ('direction', 'east')]
    assert_equal(test.peek(word_list2), 'noun')

    word_list3 = []
    assert_equal(test.peek(word_list3), None)

def test_match():
    word_list1 = scan('the bear eat the honey')
    assert_equal(test.match(word_list1, 'stop'), ('stop', 'the'))
    assert_equal(test.match(word_list1, 'noun'), ('noun', 'bear'))
    assert_equal(test.match(word_list1, 'direction'), None)

    word_list2 = []
    assert_equal(test.match(word_list2, 'noun'), None)

def test_parse_subject():
    word_list1 = scan('the bear eat the honey')
    assert_equal(test.parse_subject(word_list1), ('noun', 'bear'))

    word_list2 = scan('run in north')
    assert_equal(test.parse_subject(word_list2), ('noun', 'player'))

    word_list3 = scan('in the north')
    assert_raises(ParserError, test.parse_subject, word_list3)
