from dataclasses import dataclass
from time import time_ns
import os, secrets, hashlib, struct
from typing import Optional

@dataclass(frozen=True)
class HLC:
    physical_ns: int
    logical: int

def _now_ns() -> int:
    return time_ns()

def advance_hlc(prev: Optional[HLC]) -> HLC:
    now = _now_ns()
    if prev is None:
        return HLC(physical_ns=now, logical=0)
    if now <= prev.physical_ns:
        return HLC(physical_ns=prev.physical_ns, logical=prev.logical + 1)
    return HLC(physical_ns=now, logical=0)

def pack_hlc(h: HLC) -> bytes:
    return struct.pack('>QI', h.physical_ns, h.logical)

def get_lane_id() -> bytes:
    seed = os.environ.get('LAW_T_LANE_SEED')
    if seed:
        return hashlib.blake2s(seed.encode(), digest_size=4).digest()
    return secrets.token_bytes(4)

def mint_tlb(content: bytes, prev_hlc: Optional[HLC] = None, seq: int = 0) -> dict:
    h = advance_hlc(prev_hlc)
    epoch = pack_hlc(h)
    lane = get_lane_id()
    seq_bytes = struct.pack('>I', seq)
    rand = secrets.token_bytes(4)
    hasher = hashlib.blake2s(digest_size=4)
    hasher.update(content)
    hasher.update(epoch)
    hasher.update(lane)
    hasher.update(seq_bytes)
    hasher.update(rand)
    proof = hasher.digest()
    return {
        'epoch': epoch.hex(),
        'lane': lane.hex(),
        'seq': int.from_bytes(seq_bytes, 'big'),
        'rand': rand.hex(),
        'proof': proof.hex(),
        'hlc': {'physical_ns': h.physical_ns, 'logical': h.logical},
    }

def tlb_str(tlb: dict) -> str:
    physical_ns = tlb['hlc']['physical_ns']
    logical = tlb['hlc']['logical']
    return f"@t[ns={physical_ns}; l={logical}; lane=0x{tlb['lane']}; seq={tlb['seq']}; r={tlb['rand']}; p={tlb['proof']}]"
