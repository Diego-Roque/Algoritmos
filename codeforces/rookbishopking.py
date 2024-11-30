def chess_moves(r1, c1, r2, c2):
  
    rook_moves = 1 if r1 == r2 or c1 == c2 else 2

   
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        bishop_moves = 0  
    elif abs(r1 - r2) == abs(c1 - c2):
        bishop_moves = 1  
    else:
        bishop_moves = 2  
    
  
    king_moves = max(abs(r1 - r2), abs(c1 - c2))
    
    return rook_moves, bishop_moves, king_moves

r1, c1, r2, c2 = map(int, input().strip().split())


rook_moves, bishop_moves, king_moves = chess_moves(r1, c1, r2, c2)
print(rook_moves, bishop_moves, king_moves)
