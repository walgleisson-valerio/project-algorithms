import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("senha", "senha")

    with pytest.raises(TypeError):
        encrypt_message(1, 1)
    
    assert encrypt_message("senha", 999) == "ahnes"

    assert encrypt_message("senha", 3) == "nes_ah"

    assert encrypt_message("senha", 2) == "ahn_es"
