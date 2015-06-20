from cryptopals.set3 import (challenge_17)


def test_challenge_17(params):
    import random
    choice = random.choice(params)

    result = challenge_17.main(choice)

    assert result == choice
