import random

def randomize_features(seed, percentage):
    """Randomizes a percentage of features for a given wheat seed."""
    num_features = len(seed)
    num_randomized = int(num_features * percentage / 100)
    features_to_randomize = random.sample(range(num_features), num_randomized)
    for i in features_to_randomize:
        seed[i] = random.random()
    return seed
seed = [3.7, 5.2, 12.1, 6.5, 2.8, 8.9, 4.2, 9.6, 10.3, 7.8]
percentage = 30

print("Original seed:", seed)
randomize_features(seed, percentage)
print("Randomized seed:", seed)
