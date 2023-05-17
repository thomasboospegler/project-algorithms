from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(3, 'thomas')

    assert encrypt_message("thomas", 3) == "sam_oht"

    assert encrypt_message("12345", 0) == "54321"
