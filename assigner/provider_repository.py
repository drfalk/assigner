from time import sleep
from typing import Dict, List, Set, Tuple
from assigner import config
from threading import Semaphore

from assigner.generator import create_guid

select_for_update_semaphore = Semaphore(1)
update_provider_id_semaphore = Semaphore(1)
_uuids: List[Tuple[int, str, bool, str]] = list()
_used_uuids: Dict[int, int] = dict()

def _simulate_network_delay():
  if config.enable_add_network_delay:
    sleep(10/1000)

def insert_uuid(uuid: str) -> bool:
   _uuids.append((len(_uuids), uuid, False, ''))

def mark_uuid_provided(provider_id):
  _simulate_network_delay()
  update_provider_id_semaphore.acquire()
  for i in range(len(_uuids)):
    record = _uuids[i]
    if not record[3]:
        _uuids[i] = (record[0], record[1], record[2], provider_id)
        update_provider_id_semaphore.release()
        _simulate_network_delay()
        return _uuids[i]

def get_available_uuid() -> Tuple[int, str, bool]:
  if config.enable_use_select_for_update_query:
      select_for_update_semaphore.acquire()

  _simulate_network_delay()
  for i in range(len(_uuids)):
    record = _uuids[i]
    if record[2] is False:
        _simulate_network_delay()
        return record

def mark_uuid_used(index: int) -> Tuple[int, str]:
  record = _uuids[index]
  _simulate_network_delay()
  _uuids[index] = (record[0], record[1], True, record[3])
  _simulate_network_delay()

  if config.enable_use_select_for_update_query:
      select_for_update_semaphore.release()
  return (index, _uuids[index][1])

def get_and_use_uuid() -> Tuple[int, str, bool]:
  id = create_guid()
  top_available_records: List[int] = list()
  _simulate_network_delay()
  for i in range(len(_uuids)):
    if _uuids[i][2] is False:
        top_available_records.append(i)
        if len(top_available_records) == 5:
           break
  
  for i in top_available_records:
     if id == _used_uuids.setdefault(i,id):
        record = _uuids[i]
        _uuids[i] = (record[0], record[1], True, record[3])
        _simulate_network_delay()
        return (_uuids[i][0], _uuids[i][1], _uuids[i][2])
  
  _simulate_network_delay()
  raise Exception("No uuid available to use from subset.")