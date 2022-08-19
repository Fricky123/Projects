slots = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}
# ----------------------------------------------------------------------------------------
'''Functions'''

def draw(x):
    if slots.get(x) == "X":
        return print(f"[X already drawn on Slot {x}]")
    else:
        return slots.update({x: "X"})


def invalid():
    return input("Invalid...")
# ----------------------------------------------------------------------------------------
board = f"Slot numbers:\n" \
        f"| 1 | 2 | 3 |\n" \
        f"| 4 | 5 | 6 |\n" \
        f"| 7 | 8 | 9 |\n" \
        f"-------------------------------\n" \
        f"Your symbol is X. You go first..\n"
print(board)
while True:
    try:
        board = f"| {slots.get(1)} | {slots.get(2)} | {slots.get(3)} |\n" \
                f"| {slots.get(4)} | {slots.get(5)} | {slots.get(6)} |\n" \
                f"| {slots.get(7)} | {slots.get(8)} | {slots.get(9)} |"
        print(board)
        ans = int(input("Draw where> "))
        draw(ans)
    except ValueError:
        invalid()


