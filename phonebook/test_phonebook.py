import csv

import pytest


def read_phonebook_entries():
    entries = []
    with open("phonebook/data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Name']
            number = row['Number']

            test_case = (name, number)
            entries.append(test_case)
    return entries


@pytest.mark.parametrize("name, number", read_phonebook_entries())
def test_lookup_by_name(name, number, phonebook):
    phonebook.add(name, number)
    assert number == phonebook.lookup(name)
