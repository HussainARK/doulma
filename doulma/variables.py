import hashlib

# Hashing


def get_supported_hashing_types():
    algorithms_copy = list(hashlib.algorithms_guaranteed.copy())
    algorithms_copy.remove("shake_128")
    algorithms_copy.remove("shake_256")
    return list(algorithms_copy.copy())


supported_hashing_types = get_supported_hashing_types()
