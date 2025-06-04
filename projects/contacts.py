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

def find_contact(keyword):
    keyword = keyword.strip().lower()
    for c in load():
        if keyword in c['name'].lower():
            return c
    return None

def list_contacts():
    contacts = load()
    if not contacts:
        print('연락처 없음')
        return
    for i, c in enumerate(contacts, 1):
        email = c.get('email') or '-'
        print(f"{i}. {c['name']} / {c['phone']} / {email}")

def delete_contact(name):
    contacts = load()
    new_list = [c for c in contacts if c['name'] != name]
    if len(new_list) == len(contacts):
        print('없는 이름')
        return False
    save(new_list)
    return True
