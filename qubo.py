# Import necessary libraries
from dwave.system import DWaveSampler, EmbeddingComposite
import dimod

# Define the QUBO matrix
Q = {
    (0, 0): 10,
    (1, 1): -8,
    (2, 2): -3,
    (3, 3): -3,
    (4, 4): -2,
    (0, 1): 2,
    (0, 2): 2,
    (0, 3): 0,
    (0, 4): 0,
    (1, 2): 0,
    (1, 3): 11,
    (1, 4): 0,
    (2, 3): 2,
    (2, 4): 2,
    (3, 4): 2,
}

# Q = {(0, 0): 1, (1, 1): 2, (2, 2): 9, (0, 1): -8, (0, 2): -12}

# # 8x0x1 - 4x0x2 - 3x0 - 16x1x2 +12x2 + 4
# Q = {(0, 0): -3, (1, 1): 0, (2, 2): 12, (0, 1): 8, (0, 2): -4, (1, 2): -16}

# # Maximise 4x0 + 5x1 - 6x0x1
# Q = {(0, 0): -4, (0, 1): 5, (1, 1): -6}

# Create a binary quadratic model
bqm = dimod.BinaryQuadraticModel.from_qubo(Q)

# Solve using D-Wave
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm, num_reads=100)
print(response)
# Print the results
for sample, energy, num_occurrences in response.data(
    ["sample", "energy", "num_occurrences"]
):
    print(f"Sample: {sample}, Energy: {energy}, Occurences: {num_occurrences}")
