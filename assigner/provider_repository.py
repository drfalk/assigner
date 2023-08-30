from time import sleep
from typing import List, Tuple
from assigner import config


_uuids: List[Tuple[int, str, bool]] = list()

def _simulate_network_delay():
  if config.network_delay:
    sleep(10/1000)

def insert_uuid(uuid: str) -> bool:
   _uuids.append((len(_uuids), uuid, False))

def get_available_uuid() -> Tuple[int, str, bool]:
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
      return _uuids[index]