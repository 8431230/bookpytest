def book_details(title, author, price, pages):
    result = (
        f"Book Title: {title}\n"
        f"Author: {author}\n"
        f"Price: {price}\n"
        f"Pages: {pages}"
    )
    return result


if __name__ == "__main__":
    title = "Python Basics"
    author = "John Doe"
    price = 399
    pages = 250

    print(book_details(title, author, price, pages))
