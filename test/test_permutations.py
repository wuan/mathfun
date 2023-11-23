from assertpy import assert_that

from mathfun import BitPermutations


class TestBitPermutations:

    def test_simple(self):
        uut = BitPermutations(2, 2)
        assert_that(list(uut)).contains_only((0, 1))

    def test_one_out_of_two(self):
        uut = BitPermutations(2, 1)
        assert_that(list(uut)).contains_only((0,), (1,))

    def test_two_out_of_three(self):
        uut = BitPermutations(3, 2)
        assert_that(list(uut)).contains_only((0, 1), (0, 2), (1, 2))
