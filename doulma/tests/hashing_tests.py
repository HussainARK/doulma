import pytest
from .. import gen_password, variables
from .. import exceptions
from .. import hashing


def test_gen_hash():
    assert hashing.gen_hash(
        "Hello", 'sha256') == "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"


def test_hash_types():
    with pytest.raises(exceptions.InvalidHashType):
        hashing.gen_hash('Hello', 'potato')
