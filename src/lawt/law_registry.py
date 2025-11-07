import yaml

def load_law(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict) or 'law' not in data:
        raise ValueError("Invalid law file: missing 'law' root key")
    return data

def validate_law_shape(law_data: dict) -> list[str]:
    issues = []
    law = law_data.get('law', {})
    for key in ['name', 'form', 'meaning', 'obligation', 'proofs']:
        if key not in law:
            issues.append(f'missing required: law.{key}')
    return issues
