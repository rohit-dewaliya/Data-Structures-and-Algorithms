def letter_combinations(digits):
    if not digits:
        return []

    result = []
    letters_combo = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def backtrack(index, combo):
        if index == len(digits):
            result.append(combo)
            return

        for letter in letters_combo[digits[index]]:
            backtrack(index + 1, combo + letter)

    backtrack(0, "")
    return result

# Example
digits = "23456789"
print(letter_combinations(digits))
