import numpy as np
import math

def binary_entropy(x):
    if x <= 0 or x >= 1:
        return 0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)

def run_bb84(n, attack_probability):

    # Alice generates random bits
    alice_bits = np.random.randint(0, 2, n)

    # Alice randomly selects bases
    alice_bases = np.random.choice(["+", "×"], n)

    # Eve attack decision
    eve_attack = np.random.rand(n) < attack_probability
    eve_bases = np.random.choice(["+", "×"], n)

    # Bob randomly chooses bases
    bob_bases = np.random.choice(["+", "×"], n)

    bob_results = []

    for i in range(n):

        bit = alice_bits[i]
        basis = alice_bases[i]

        # Eve intercept-resend attack
        if eve_attack[i]:

            if eve_bases[i] == basis:
                eve_result = bit
            else:
                eve_result = np.random.randint(0, 2)

            # Eve resends photon using her basis
            bit = eve_result
            basis = eve_bases[i]

        # Bob measures photon
        if bob_bases[i] == basis:
            bob_bit = bit
        else:
            bob_bit = np.random.randint(0, 2)

        bob_results.append(bob_bit)

    bob_results = np.array(bob_results)

    # Basis comparison
    matching = alice_bases == bob_bases

    alice_key = alice_bits[matching]
    bob_key = bob_results[matching]

    # QBER calculation
    if len(alice_key) == 0:
        qber = 0
        skr = 0
    else:
        errors = np.sum(alice_key != bob_key)
        qber = errors / len(alice_key)
        skr = max(0, 1 - 2 * binary_entropy(qber))

    return (
        alice_bits,
        alice_bases,
        eve_attack,
        eve_bases,
        bob_bases,
        bob_results,
        matching,
        alice_key,
        bob_key,
        qber,
        skr
    )