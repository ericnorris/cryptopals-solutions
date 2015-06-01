from os import path
from re import match

import pickle
import pytest

test_directory = path.dirname(path.realpath(__file__))


@pytest.fixture
def params(request):
    function_name = request.function.__name__
    challenge = match('test_(\w+)', function_name).group(1)

    picklefile = test_directory + '/input/' + challenge + '_input.pickle'

    return pickle.load(open(picklefile))


@pytest.fixture
def expected(request):
    function_name = request.function.__name__
    challenge = match('test_(\w+)', function_name).group(1)

    picklefile = test_directory + '/output/' + challenge + '_output.pickle'

    return pickle.load(open(picklefile))
