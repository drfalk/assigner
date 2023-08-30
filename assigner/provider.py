from typing import Set, Tuple
from assigner import config, provider_repository
from threading import Semaphore
from assigner.generator import create_guid

_pre_loaded_uuids: Set[Tuple[int, str]] = set()
pre_load_in_progress_semaphore = Semaphore(1)
provider_id = create_guid()


def create_uuids() -> None:
    for _ in range(1000):
        new_uuid = create_guid()
        provider_repository.insert_uuid(new_uuid)
    
    if config.enable_preloading_of_uuids_to_provider:
        load_uuids_to_provider()

def use_uuid() -> str:
    if config.enable_use_preloaded_uuids:
        used_uuid_tuple = use_provider_pre_loaded_uuid()
    elif config.enable_use_stored_procedure_to_select_and_update:
        used_uuid_tuple = provider_repository.get_and_use_uuid()
    else:
        uuid_tuple = provider_repository.get_available_uuid()
        used_uuid_tuple = provider_repository.mark_uuid_used(uuid_tuple[0])
    
    if config.enable_preloading_of_uuids_to_provider and len(_pre_loaded_uuids) < 20:
        load_uuids_to_provider()
        
    return used_uuid_tuple[1]

def load_uuids_to_provider() -> None:
    if pre_load_in_progress_semaphore.acquire(blocking=False):
        for _ in range(100):
            (index, uuid, _, _) = provider_repository.mark_uuid_provided(provider_id=provider_id)
            _pre_loaded_uuids.add((index, uuid))
        print('Loaded uuids into provider')
        pre_load_in_progress_semaphore.release()

def use_provider_pre_loaded_uuid() -> Tuple[int, str]:
    used_uuid = _pre_loaded_uuids.pop()
    print('remaining uuids ' + str(len(_pre_loaded_uuids)))
    if config.enable_synchronous_update_when_using_preloaded_uuid:
        provider_repository.mark_uuid_used(used_uuid[0])
    return used_uuid