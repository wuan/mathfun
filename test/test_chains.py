from assertpy import assert_that

from mathfun.chains import sum_chain


class TestChains:

    def test_simple(self):
        result = sum_chain("123", 1)
        assert_that(result).is_length(1)
        assert_that(result[0].sum).is_equal_to(123)
        assert_that(result[0].summands).contains_only(123)

