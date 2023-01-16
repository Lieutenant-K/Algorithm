def solution(phone_book):
    book = sorted(phone_book)
    return not bool([i for i in range(len(book)-1) if book[i+1].startswith(book[i])])
