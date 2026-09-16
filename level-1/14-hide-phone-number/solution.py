def solution(phone_number):
    hidden_count = len(phone_number) - 4
    hidden = "*" * hidden_count
    visible = phone_number[-4:]
    return hidden + visible
