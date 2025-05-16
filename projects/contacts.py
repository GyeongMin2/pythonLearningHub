import json
from pathlib import Path

DATA = Path('projects/contacts.json')

def load():
    if not DATA.exists():
        return []
    try:
        return json.loads(DATA.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
        print('JSON 깨짐 — 빈 목록으로 시작')
        return []

def save(contacts):
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(contacts, ensure_ascii=False, indent=2), encoding='utf-8')

def add_contact(name, phone, email=''):
    contacts = load()
    for c in contacts:
        if c['name'] == name:
            print('이미 있음, 업데이트')
            c['phone'] = phone
            c['email'] = email
            save(contacts)
            return
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save(contacts)
