from cryptopals.set1 import (challenge_1, challenge_2, challenge_3,
                             challenge_4, challenge_5, challenge_6,
                             challenge_7, challenge_8)


def test_challenge_1(params, expected):
    result = challenge_1.hex_to_base64(*params)

    assert result == expected


def test_challenge_2(params, expected):
    result = challenge_2.main(*params)

    assert result == expected


def test_challenge_3(params, expected):
    result = challenge_3.main(*params)

    assert result == expected


def test_challenge_4(params, expected):
    result = challenge_4.main(*params)

    assert result == expected


def test_challenge_5(params, expected):
    result = challenge_5.main(*params)

    assert result == expected


def test_challenge_6(params, expected):
    ciphertext = params[0].decode('base64')

    result = challenge_6.main(ciphertext)

    assert result == expected


def test_challenge_7(params, expected):
    b64_ciphertext, key = params

    result = challenge_7.main(b64_ciphertext.decode('base64'), key)

    assert result == expected


def test_challenge_8(params, expected):
    # TODO: maybe change output of challenge 8?
    result = challenge_8.main(*params)

    assert result == expected
