from typing import List, Tuple


_uuids: List[Tuple[int, str, bool]] = list()

def insert_uuid(uuid: str) -> bool:
   _uuids.append((len(_uuids), uuid, False))

def get_available_uuid() -> Tuple[int, str, bool]:
  for i in range(len(_uuids)):
    record = _uuids[i]
    if record[2] is False:
        return record

def mark_uuid_used(index: int) -> Tuple[int, str, bool]:
      record = _uuids[index]
      _uuids[index] = (record[0], record[1], True)
      return _uuids[index]