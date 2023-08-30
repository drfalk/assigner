from assigner.provider import create_guid

def test_get_uuid():
    assert len(create_guid()) == 36