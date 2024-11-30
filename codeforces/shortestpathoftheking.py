def chessboard_to_coords(position):
  
    col = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return col, row

def find_king_moves(start, target):
    x1, y1 = chessboard_to_coords(start)
    x2, y2 = chessboard_to_coords(target)
    
    moves = []
    while x1 != x2 or y1 != y2:
        move = ""
        if y2 > y1:
            move += "U"
            y1 += 1
        elif y2 < y1:
            move += "D"
            y1 -= 1
        if x2 > x1:
            move += "R"
            x1 += 1
        elif x2 < x1:
            move += "L"
            x1 -= 1
        moves.append(move)
    
    return moves


start = input().strip()
target = input().strip()


moves = find_king_moves(start, target)


print(len(moves))
print("\n".join(moves))
