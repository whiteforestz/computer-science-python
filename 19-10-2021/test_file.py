def summarize(x: float, y: float) -> float:
    return x + y


with open('test_cases.txt') as f:
    for (i, line) in enumerate(f.readlines()):
        tokens = line.replace('\n', '').split(' ')
        a, b, r = map(float, tokens)
        if summarize(a, b) != r:
            print(f'error at {i + 1} line')
