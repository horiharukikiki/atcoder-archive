N = int(input())
card_list = [int(i) for i in input().split()]
if N%2: card_list.append(0)
sort_card_list = sorted(card_list)
Alice = 0
Bob = 0
while sort_card_list:
    Alice += sort_card_list.pop(-1)
    Bob += sort_card_list.pop(-1)
print(Alice-Bob)