def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        return [(source, target)]
    
    moves = tower_of_hanoi(n - 1, source, auxiliary, target)
    
    moves.append((source, target))
    
    moves += tower_of_hanoi(n - 1, auxiliary, target, source)
    
    return moves
