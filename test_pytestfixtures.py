import pytest


@pytest.fixture()
def setup():
    print("everttime")


def testmethod1(setup):
    print("This is test method")


def testmethod2(setup):
    print("This is second test method")
