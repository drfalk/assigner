from typing import List, Tuple

from assigner.generator import create_guid


class _Provider:
    uuids: List[Tuple[str,bool]]

    def __init__(self):
        self.uuids = list()

    def load_uuids(self) -> None:
        for _ in range(1000):
            self.uuids.append((create_guid(),False))
    
    def select_then_update(self) -> str:
        for i in range(len(self.uuids)):
            record = self.uuids[i]
            if record[1] is False:
                self.uuids[i] = (record[0], True)
                return record[0]
        


provider = _Provider()