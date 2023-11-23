from qdrant_client.http.models import SparseVector
from typing import List
import random
import numpy as np


def empty_sparse_vector() -> SparseVector:
    return SparseVector(
        indices=np.array([], dtype=np.int64),
        values=np.array([], dtype=np.float32),
    )


def validate_sparse_vector(vector: SparseVector) -> None:
    assert len(vector.indices) == len(vector.values)
    assert len(vector.indices) == len(set(vector.indices))


def is_sorted(vector: SparseVector) -> bool:
    for i in range(1, len(vector.indices)):
        if vector.indices[i] < vector.indices[i - 1]:
            return False
    return True


def sort(vector: SparseVector) -> SparseVector:
    if is_sorted(vector):
        return vector

    sorted_indices = np.argsort(vector.indices)
    return SparseVector(
        indices=vector.indices[sorted_indices],
        values=vector.values[sorted_indices],
    )


def calculate_distance_sparse(query: SparseVector, vectors: List[SparseVector]) -> List[float]:
    scores = []

    for vector in vectors:
        score = sparse_dot_product(query, vector)
        scores.append(score)

    return scores


# Expects sorted indices
def sparse_dot_product(vector1: SparseVector, vector2: SparseVector) -> float:
    result = 0.0
    i, j = 0, 0

    while i < len(vector1.indices) and j < len(vector2.indices):
        if vector1.indices[i] == vector2.indices[j]:
            result += vector1.values[i] * vector2.values[j]
            i += 1
            j += 1
        elif vector1.indices[i] < vector2.indices[j]:
            i += 1
        else:
            j += 1

    return result


def generate_random_sparse_vector(size: int, density: float) -> SparseVector:
    num_non_zero = int(size * density)
    indices: List[int] = random.sample(range(size), num_non_zero)
    values: List[float] = [random.random() for _ in range(num_non_zero)]
    indices.sort()
    return SparseVector(indices=indices, values=values)


def generate_random_sparse_vector_list(num_vectors: int, vector_size: int, vector_density: float) -> List[SparseVector]:
    sparse_vector_list = []
    for _ in range(num_vectors):
        sparse_vector = generate_random_sparse_vector(vector_size, vector_density)
        sparse_vector_list.append(sparse_vector)
    return sparse_vector_list