import json, hashlib, time
from pathlib import Path
from typing import List

class Ledger:
    def __init__(self, root: str):
        self.root = Path(root)
        (self.root / 'objects').mkdir(parents=True, exist_ok=True)
        (self.root / 'index').mkdir(parents=True, exist_ok=True)

    def _sha256(self, b: bytes) -> str:
        return hashlib.sha256(b).hexdigest()

    def add(self, payload: bytes, meta: dict) -> str:
        h = self._sha256(payload)
        obj = self.root / 'objects' / h
        if not obj.exists():
            obj.write_bytes(payload)
        idx = {'hash': h, 'meta': meta, 'ts': time.time()}
        (self.root / 'index' / f'{h}.json').write_text(json.dumps(idx, indent=2))
        return h

    def list(self) -> List[str]:
        return [p.stem for p in (self.root / 'index').glob('*.json')]
