from pytest import mark, fixture
from lib.most_often import MostOften

@fixture
def test_most_often_integers():
    return MostOften([5,6,7,3,7,7])

@fixture
def test_most_often_strs():
    return MostOften(
        ["blob", "blob", "egg", "foot", "cow"]
    )

@fixture
def test_empty_class():
    return MostOften([])

class TestInit():

    @mark.it("Test class inits with passed item as starting list attribute")
    def test_init(self, test_most_often_integers):
        assert test_most_often_integers.starting_list == [5,6,7,3,7,7]


class TestAddNew():

    @mark.it("test add new appends past item to starting list")
    def test_add(self,test_most_often_integers):
        blob = "blob"
        test_most_often_integers.add_new(blob)

        assert test_most_often_integers.starting_list[-1] == blob


class TestGetMostOften():

    @mark.it('Returns "no clear winner" when highest_items list empty')
    def test_empty_items(self, test_empty_class):
        assert test_empty_class.get_most_often() == "no clear winner"

    @mark.it('Returns highest count item  when winner with ints')
    def test_winner_ints(self, test_most_often_integers):
        assert test_most_often_integers.get_most_often() == 7

    @mark.it('Returns highest count item  with strings')
    def test_winner_strings(self, test_most_often_strs):
        assert test_most_often_strs.get_most_often() == "blob"

    @mark.it("Returns highest count item with mixed types")
    def test_winner_mixed(self):
        mixed_test = MostOften(
            ["egg", 5, None, "plant", 9.9, "egg"]
        )
        assert mixed_test.get_most_often() == "egg"

    @mark.it("Returns winner after all methods called")
    def test_after_add_new(self):
        after_add_test = MostOften(
            ["one", "two", "three", "four", "five"]
        )
        after_add_test.add_new("one")
        assert after_add_test.get_most_often() == "one"