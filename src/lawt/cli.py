import os, json
from .ledger import Ledger
from .tlb import mint_tlb, tlb_str
from .law_registry import load_law, validate_law_shape

DEFAULT_LEDGER = os.environ.get('LAW_T_LEDGER', '.lawt-ledger')

def cmd_law_add(path: str):
    law_data = load_law(path)
    issues = validate_law_shape(law_data)
    if issues:
        print('Validation issues:')
        for i in issues:
            print(' -', i)
        return 2
    payload = json.dumps(law_data, sort_keys=True).encode()
    tlb = mint_tlb(payload, prev_hlc=None, seq=0)
    meta = {'type': 'law', 'tlb': tlb}
    ledger = Ledger(DEFAULT_LEDGER)
    obj_hash = ledger.add(payload, meta)
    print('Stored law ->', obj_hash)
    print('TLB:', tlb_str(tlb))
    return 0

def cmd_ledger_list():
    ledger = Ledger(DEFAULT_LEDGER)
    for h in ledger.list():
        print(h)
