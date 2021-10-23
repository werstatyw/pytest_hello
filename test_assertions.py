def test_long_strings():
    string = ("This is a very, very, long string that has some differences"
            " that are hard to catch")
    expected = ("This is a very, very long string that hes some differences"
            " that are hard to catch")
    assert string == expected