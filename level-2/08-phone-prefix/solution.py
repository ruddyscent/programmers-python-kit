def solution(phone_book):
    registered = set(phone_book)
    for phone in phone_book:
        for end in range(1, len(phone)):
            if phone[:end] in registered:
                return False
    return True
