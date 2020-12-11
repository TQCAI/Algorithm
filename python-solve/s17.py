mapper = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

results = [""]

for digit in digits:
    cur_results = []
    for result in results:
        for alpha in mapper[digit]:
            cur_results.append(result + alpha)
    results = cur_results

print(results)