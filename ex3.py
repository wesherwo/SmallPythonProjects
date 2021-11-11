p1 = 'n'
while p1 != 'r' and p1 != 'p' and p1 != 's':
    p1 = input("Player 1 (r,p,s): ")
p2 = 'n'
while p2 != 'r' and p2 != 'p' and p2 != 's':
    p2 = input("Player 2 (r,p,s): ")
if p1 == p2:
    print("Tie!")
else:
    if (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
        print("player 1 wins!")
    else:
        print("Player 2 wins!")