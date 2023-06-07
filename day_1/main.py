def summation(data: list) -> list:
    sums = [sum(d) for d in data]

    return sums

def return_max(data: list) -> int:
    return max(data)

def top_three(data: list) -> int:
    sums = summation(data)

    return sum(sorted(sums, reverse=True)[:3])

def extract_data(filename: str) -> list[list[int]]:
    with open(filename, encoding="utf-8") as f:
        data = f.read().split("\n\n")

    return [list(map(int, d.splitlines())) for d in data]

if __name__ == "__main__":
    data = extract_data("./calories.txt")
    sums = summation(data)

    print("The sum of the elf with the highest amount of calories is:", return_max(sums))

    print("The sum of the top three elves is:", top_three(data))