from book import book_details

def test_book_details():
    expected_output = (
        "Book Title: Python Basics\n"
        "Author: John Doe\n"
        "Price: 399\n"
        "Pages: 250"
    )

    assert book_details("Python Basics", "John Doe", 399, 250) == expected_output
