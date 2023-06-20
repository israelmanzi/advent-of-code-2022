def calc_score(pl_ch: str, score: int) -> int:
    match pl_ch:
        case "R":
            return score + 1
        case "P":
            return score + 2
        case "S":
            return score + 3
        case _:
            return score
    
def resolve_choice(move: str) -> str:
    match move:
        case "A" | "X":
            return "R"
        case "B" | "Y":
            return "P"
        case "C" | "Z":
            return "S"
        case _:
            raise ValueError("Player choice must be A, B, C, X, Y or Z.")

def calc_winner(p1_score: str, p2_score: str) -> str:
    if p1_score == p2_score:
        return "D"
    elif (p1_score == "P" and p2_score == "R") or (p1_score == "S" and p2_score == "P") or (p1_score == "R" and p2_score == "S"):
        return "1"
    elif (p1_score == "S" and p2_score == "R") or (p1_score == "R" and p2_score == "P") or (p1_score == "P" and p2_score == "S"):
        return "2"
    else:
        raise ValueError("Error receiving input!")
    
def resolve_winner(p1_move: str, p2_move: str) -> str:    
    return calc_winner(p1_move, p2_move)

def cf(input: tuple) -> int:
    p1_move, p2_move = input
    p2_score = 0

    move_1 = resolve_choice(p1_move)
    move_2 = resolve_choice(p2_move)
        
    result = resolve_winner(move_1, move_2)
    if result == "1":
        p2_score = calc_score(move_2, 0)
    elif result == "2":
        p2_score = calc_score(move_2, 6)
    else:
        p2_score = calc_score(move_2, 3)

    return p2_score

def extract_data(filename: str) -> list[tuple[str]]:
    with open(filename, encoding="utf-8") as f:
        data = [tuple(l.split()) for l in f.readlines()]

    return data

if __name__ == "__main__":
    data = extract_data("./rpc.txt")

    scores = [cf(d) for d in data]

    print(sum(scores))