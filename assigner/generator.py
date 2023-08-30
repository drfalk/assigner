from assigner import provider_repository

from assigner.generator import create_guid

def load_uuids() -> None:
    for _ in range(1000):
        new_uuid = create_guid()
        provider_repository.insert_uuid(new_uuid)

def use_uuid() -> str:
    uuid_tuple = provider_repository.get_available_uuid()
    used_uuid_tuple = provider_repository.mark_uuid_used(uuid_tuple[0])
    return used_uuid_tuple[1]