from .. import gen_password


def test_gen_pass():
    assert len(gen_password(54)) == 54
