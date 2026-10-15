def borrow_book(available_books: int) -> int:
    if available_books <= 0:
        raise ValueError("No books available")

    return available_books - 1


def return_book(available_books: int) -> int:
    return available_books + 1


def test_borrow_book() -> None:
    assert borrow_book(10) == 9
    assert borrow_book(5) == 4


def test_return_book() -> None:
    assert return_book(9) == 10
    assert return_book(4) == 5


def test_invalid_borrow() -> None:
    try:
        borrow_book(0)
        assert False
    except ValueError:
        assert True


def main() -> None:
    available_books = 8

    print("Initial Books:", available_books)

    available_books = borrow_book(available_books)
    print("After Borrowing:", available_books)

    available_books = return_book(available_books)
    print("After Returning:", available_books)

    test_borrow_book()
    test_return_book()
    test_invalid_borrow()

    print("All tests passed")


if __name__ == "__main__":
    main()