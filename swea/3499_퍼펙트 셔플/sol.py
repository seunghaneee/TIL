import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())

    deck_1_list = deck[:len(deck)//2]
    deck_2_list = deck[len(deck)//2:]
    if len(deck) % 2 != 0:
        deck_2_list = deck[len(deck)//2+1:]
        deck_1_list = deck[:len(deck)//2 + 1]


    suffle = []

    for _ in range(len(deck_2_list)):
        suffle.append(deck_1_list.pop(0))
        suffle.append(deck_2_list.pop(0))

    if len(deck_1_list) != 0:
        suffle.append(deck_1_list.pop())

    print(f'#{tc}', *suffle)