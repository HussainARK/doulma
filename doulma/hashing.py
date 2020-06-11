from . import exceptions
from . import variables


def gen_hash(text: str, hash_type: str = 'sha256') -> str:
    import hashlib
    """
	gen_hash
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	A Simple function that depends on the "hashlib" library,
	it generates hashes based on the text and the type.
	
	
	:param text: Some Text to Hash
	:param hash_type: a String from the "doulma.variables.supported_hashing_types" list
	:return: A Hash String "str"
	"""
    if (type(text) == str) or (type(hash_type) == str):
        if hash_type.strip() in variables.supported_hashing_types:
            return hashlib.new(hash_type, text.encode()).hexdigest()
        else:
            raise exceptions.InvalidHashType(
                ':hash_type: must be a valid Hash Type, Valid Types are: ' + ', '.join(hashlib.algorithms_available))
    else:
        raise exceptions.InvalidArgument(
            ':text:/:hash_type: must be a string/variables.HashType')
