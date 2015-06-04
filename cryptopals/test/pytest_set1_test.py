from cryptopals.set1 import (challenge_01, challenge_02, challenge_03,
                             challenge_04, challenge_05, challenge_06,
                             challenge_07, challenge_08)


def test_challenge_01(params, expected):
    result = challenge_01.hex_to_base64(*params)

    assert result == expected


def test_challenge_02(params, expected):
    result = challenge_02.main(*params)

    assert result == expected


def test_challenge_03(params, expected):
    result = challenge_03.main(*params)

    assert result == expected


def test_challenge_04(params, expected):
    result = challenge_04.main(*params)

    assert result == expected


def test_challenge_05(params, expected):
    result = challenge_05.main(*params)

    assert result == expected


def test_challenge_06(params, expected):
    ciphertext = params[0].decode('base64')

    result = challenge_06.main(ciphertext)

    assert result == expected


def test_challenge_07(params, expected):
    b64_ciphertext, key = params

    result = challenge_07.main(b64_ciphertext.decode('base64'), key)

    assert result == expected


def test_challenge_08(params, expected):
    # TODO: maybe change output of challenge 8?
    result = challenge_08.main(*params)

    assert result == expected
