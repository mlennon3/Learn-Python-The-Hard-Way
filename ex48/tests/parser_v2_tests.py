from nose.tools import *
from ex48 import parser_v2


#this program can have some weird errors from re-using these word_lists in different test functions.  Recommended to lose these and use a unique list in each function
word_list_1 = parser_v2.WordList([('noun', 'princess')])
word_list_2 = parser_v2.WordList([('noun', 'princess')])
word_list_3 = parser_v2.WordList([('verb', 'go'), ('noun', 'princess')])
word_list_4 = parser_v2.WordList([('direction', 'north'), ('noun', 'princess')])
word_list_5 = parser_v2.WordList([('direction', 'north'), ('noun', 'princess')])
word_list_6 = parser_v2.WordList([('verb', 'go'), ('noun', 'princess')])
word_list_7 = parser_v2.WordList([('verb', 'go'), ('noun', 'princess'), ('direction', 'north')])
word_list_8 = parser_v2.WordList([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')])
word_list_9 = parser_v2.WordList([('verb', 'go'), ('noun', 'princess'),('direction', 'north')])
word_list_10 = parser_v2.WordList([('direction', 'north'), ('verb', 'go'), ('noun', 'princess')])
word_list_11 = parser_v2.WordList('')

def test_peek():
    assert_equal(word_list_1.peek(), 'noun')
    assert_equal(word_list_2.peek(), 'noun')    
    assert_equal(word_list_11.peek(), None)


def test_match():
    assert_equal(word_list_2.match('noun'), ('noun', 'princess'))
    assert_equal(word_list_2.match('stop'), None)
    assert_equal(word_list_2.match('noun'), None)


def test_skip():
    #skip doesn't return anything
    assert_equal(word_list_2.skip('noun'), None)


def test_parse_verb():
    assert_equal(word_list_3.parse_verb(), ('verb', 'go'))
    assert_raises(parser_v2.ParserError, word_list_2.parse_verb)


def test_parse_object():
    assert_equal(word_list_1.parse_object(), ('noun', 'princess'))
    assert_equal(word_list_5.parse_object(), ('direction', 'north'))
    assert_raises(parser_v2.ParserError, word_list_6.parse_object)

sentence = parser_v2.Sentence(('noun', 'princess'), ('verb', 'go'), ('direction', 'north'))


def test_parse_subject():
    assert_is_instance(word_list_7.parse_subject(('noun', 'princess')), parser_v2.Sentence)


def test_parse_sentence():
    assert_is_instance(word_list_8.parse_sentence(), parser_v2.Sentence)
    assert_is_instance(word_list_9.parse_sentence(), parser_v2.Sentence)
    assert_raises(parser_v2.ParserError, word_list_10.parse_sentence)
    
