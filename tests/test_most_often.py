from pytest import mark, fixture
from lib.most_often import MostOften

@fixture
def test_most_often_integers():
    return MostOften([5,6,7,3,7,7])

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