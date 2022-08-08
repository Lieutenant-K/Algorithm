def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        head = phone_book[i]
        number = phone_book[i+1]
        if number.find(head, 0, len(head)) == 0:
            answer = False
            break

    return answer