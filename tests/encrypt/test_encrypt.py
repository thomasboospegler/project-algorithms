from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(2, "cadu")

    assert encrypt_message("cadu", 2) == "ud_ac"

    assert encrypt_message("12345", 0) == "54321"
