import random

def simulate_game(n):
    """Simulate a single game and return the winner"""
    alice_score, bob_score = 0, 0
    previous_toss = random.choice(["H", "T"])
    for _ in range(n-1):
        current_toss = random.choice(["H", "T"])
        if previous_toss == "H":
            if current_toss == "H":
                alice_score += 1
            else:
                bob_score += 1
        previous_toss = current_toss

    if alice_score > bob_score:
        return 'Alice'
    elif bob_score > alice_score:
        return 'Bob'
    else:
        return 'Tie'

def simulate_probability(n, simulations=100000):
    """Simulate multiple games to estimate probabilities"""
    results = {'Alice': 0, 'Bob': 0, 'Tie': 0}
    for _ in range(simulations):
        result = simulate_game(n)
        results[result] += 1

    for key in results:
        results[key] = results[key] / simulations
    return results

def main():
    n_values = [2, 3, 4, 5, 1024]
    for n in n_values:
        probability = simulate_probability(n)
        print(f"Probabilities for n={n}: {probability}")

if __name__ == "__main__":
    main()
