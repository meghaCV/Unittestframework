import pytest


@pytest.yield_fixture()
def setup():
    print("everttime")
    yield ()
    print("once after every method")


def testmethod1(setup):
    print("This is test method")


def testmethod2(setup):
    print("This is second test method")
