from app.main import check_password


def test_valid_example() -> None:
    assert check_password("Pass@word1") is True


def test_too_short() -> None:
    assert check_password("Str@ng") is False


def test_only_letters_invalid() -> None:
    assert check_password("qwertyui") is False


def test_missing_uppercase() -> None:
    assert check_password("password1@") is False


def test_missing_digit() -> None:
    assert check_password("Password@") is False


def test_missing_character() -> None:
    assert check_password("Password1") is False


def test_too_long_password() -> None:
    assert check_password("Pass@word123456789") is False


def test_min_length_valid() -> None:
    assert check_password("P@ssw1rd") is True


def test_max_16_length_valid() -> None:
    assert check_password("Valid@Passw0rd12") is True


def test_invalid_character() -> None:
    assert check_password("Password1*") is False
