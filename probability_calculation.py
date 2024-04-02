import random
def simulate_game(n):
    """Simulate a single game and return the result"""
    sequence = ''.join(random.choice(["H","T"]) for _ in range(n))
    aliceScore = sequence.count('HH')
    bobScore = sequence.count('HT')
    if aliceScore > bobScore:
        return 'Alice'
    elif aliceScore < bobScore:
        return 'Bob'
    else:
        return 'Tie'
def simulate_probability(n, simulations=10000):
    """Simulate Multiple Games to Estimate Probabilities"""
    results = {
        'Alice': 0,
        'Bob': 0,
        'Tie': 0
    }
    for _ in range(simulations):
        result = simulate_game(n)
        results[result] += 1

    for key in results:
        results[key] /= simulations

    return results

print(simulate_probability(1000))