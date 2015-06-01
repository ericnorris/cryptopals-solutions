from os import path
from re import match

import pickle
import pytest

test_dir = path.dirname(path.realpath(__file__))


@pytest.fixture
def params(request):
    function_name = request.function.__name__
    challenge = match('test_(\w+)', function_name).group(1)

    picklefile = open(test_dir + '/input/' + challenge + '_input.pickle')
    result = pickle.load(picklefile)

    picklefile.close()

    return result


@pytest.fixture
def expected(request):
    function_name = request.function.__name__
    challenge = match('test_(\w+)', function_name).group(1)

    picklefile = open(test_dir + '/output/' + challenge + '_output.pickle')
    result = pickle.load(picklefile)

    picklefile.close()

    return result
