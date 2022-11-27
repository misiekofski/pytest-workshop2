import pytest

from phonebook.phonebook import PhoneBook


@pytest.fixture
def phonebook(tmpdir):
    phonebook = PhoneBook(tmpdir)
    yield phonebook
    phonebook.clear()

