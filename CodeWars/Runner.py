from one import *
def t_likes():
    # test 1.py
    assert_equals(likes([]), 'no one likes this')
    assert_equals(likes(['Peter']), 'Peter likes this')
    assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

def assert_equals(str1, str2):
        assert str1 == str2, "{} und {} muessen gleich sein.".format(str1, str2)


t_likes()


def t_find_outlier():
    assert_equals(find_outlier([2, 6, 8, 10, 3]), 3)



t_find_outlier()



def t_iq():
    assert_equals(iq_test("2 4 7 8 10"), 3)
    assert_equals(iq_test("1 2 2"), 1)


t_iq()

from random import randint
def t_alphabet_position():
    assert_equals(alphabet_position("The sunset sets at twelve o' clock."),
                       "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    assert_equals(alphabet_position("The narwhal bacons at midnight."),
                       "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

    number_test = ""
    for item in range(10):
        number_test += str(randint(1, 9))
    assert_equals(alphabet_position(number_test), "")

t_alphabet_position()


def t_spin_words():
    assert_equals(spin_words("Welcome"), "emocleW")


t_spin_words()



def t_comp():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    assert_equals(comp(a1, a2), True)

    assert_equals(comp([121], [121]), False)


t_comp()


def t_scramble():
    assert_equals(scramble('rkqodlw', 'world'), True)
    assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
    assert_equals(scramble('katas', 'steak'), False)
    assert_equals(scramble('scriptjava', 'javascript'), True)
    assert_equals(scramble('scriptingjava', 'javascript'), True)

t_scramble()