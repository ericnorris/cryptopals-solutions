

from cryptopals.set2 import (challenge_9, challenge_10, challenge_11,
                             challenge_12, challenge_13, challenge_14,
                             challenge_15, challenge_16)

import pytest


def test_challenge_9(params, expected):
    result = challenge_9.main(*params)

    assert result == expected


def test_challenge_10(params, expected):
    b64_ciphertext, key, iv, = params

    result = challenge_10.main(b64_ciphertext.decode('base64'), key, iv)

    assert result == expected


def test_challenge_11():
    # TODO: utilize parameterization here
    # Test five times
    assert challenge_11.main() == True
    assert challenge_11.main() == True
    assert challenge_11.main() == True
    assert challenge_11.main() == True
    assert challenge_11.main() == True


def test_challenge_12(params):
    # TODO: encrypt here, then check?
    plaintext = params[0].decode('base64')

    result = challenge_12.main(plaintext)

    assert result == plaintext


def test_challenge_13():
    admin_profile = challenge_13.main()

    assert 'role' in admin_profile
    assert 'admin' == admin_profile['role']


def test_challenge_14(params):
    # TODO: encrypt here, then check?
    plaintext = params[0].decode('base64')

    result = challenge_14.main(plaintext)

    assert result == plaintext


def test_challenge_15():
    # TODO utilize parameterization here
    good_input = "ICE ICE BABY\x04\x04\x04\x04"
    expected = "ICE ICE BABY"

    result = challenge_15.main(good_input)

    assert result == expected

    with pytest.raises(Exception):
        bad_input = "ICE ICE BABY\x05\x05\x05\x05"

        challenge_15.main(bad_input)

    with pytest.raises(Exception):
        bad_input = "ICE ICE BABY\x01\x02\x03\x04"

        challenge_15.main(bad_input)


def test_challenge_16():
    # TODO: do admin_check here?
    assert challenge_16.main() == True
