from nose.tools import *
from ex48 import parser


#this program can have some weird errors from re-using these word_lists in different test functions.  Recommended to lose these and use a unique list in each function
word_list_1 = [('noun', 'princess')]
word_list_2 = [('noun', 'princess')]
word_list_3 = [('verb', 'go'), ('noun', 'princess')]
word_list_4 = [('direction', 'north'), ('noun', 'princess')]
word_list_5 = [('direction', 'north'), ('noun', 'princess')]
word_list_6 = [('verb', 'go'), ('noun', 'princess')]
word_list_7 = [('verb', 'go'), ('noun', 'princess'), ('direction', 'north')]
word_list_8 = [('noun', 'princess'), ('verb', 'go'), ('direction', 'north')]
word_list_9 = [('verb', 'go'), ('noun', 'princess'),('direction', 'north')]
word_list_10 = [('direction', 'north'), ('verb', 'go'), ('noun', 'princess')]

def test_peek():
    assert_equal(parser.peek(word_list_1), 'noun')
    assert_equal(parser.peek(word_list_2), 'noun')    
    assert_equal(parser.peek(''), None)


def test_match():
    assert_equal(parser.match(word_list_2,'noun'), ('noun', 'princess'))
    assert_equal(parser.match(word_list_2, 'stop'), None)
    assert_equal(parser.match('', 'noun'), None)


def test_skip():
    #skip doesn't return anything
    assert_equal(parser.skip(word_list_2, 'noun'), None)


def test_parse_verb():
    assert_equal(parser.parse_verb(word_list_3), ('verb', 'go'))
    assert_raises(parser.ParserError, parser.parse_verb, word_list_2)


def test_parse_object():
    assert_equal(parser.parse_object(word_list_1), ('noun', 'princess'))
    assert_equal(parser.parse_object(word_list_5), ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, word_list_6)

sentence = parser.Sentence(('noun', 'princess'), ('verb', 'go'), ('direction', 'north'))


def test_parse_subject():
    assert_is_instance(parser.parse_subject(word_list_7, ('noun', 'princess')), parser.Sentence)


def test_parse_sentence():
    assert_is_instance(parser.parse_sentence(word_list_8), parser.Sentence)
    assert_is_instance(parser.parse_sentence(word_list_9), parser.Sentence)
    assert_raises(parser.ParserError, parser.parse_sentence, word_list_10)
    

