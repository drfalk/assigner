from time import sleep
from typing import List, Tuple
from assigner import config
from threading import Semaphore

select_for_update_semaphore = Semaphore(1)
_uuids: List[Tuple[int, str, bool]] = list()

def _simulate_network_delay():
  if config.enable_add_network_delay:
    sleep(10/1000)

def insert_uuid(uuid: str) -> bool:
   _uuids.append((len(_uuids), uuid, False))

def get_available_uuid() -> Tuple[int, str, bool]:
  if config.enable_use_select_for_update_query:
      select_for_update_semaphore.acquire()

  _simulate_network_delay()
  for i in range(len(_uuids)):
    record = _uuids[i]
    if record[2] is False:
        _simulate_network_delay()
        return record

def mark_uuid_used(index: int) -> Tuple[int, str, bool]:
  record = _uuids[index]
  _simulate_network_delay()
  _uuids[index] = (record[0], record[1], True)
  _simulate_network_delay()
  
  if config.enable_use_select_for_update_query:
      select_for_update_semaphore.release()
  return _uuids[index]