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

def search_contacts(keyword):
    keyword = keyword.strip().lower()
    return [c for c in load() if keyword in c['name'].lower() or keyword in c['phone']]

def normalize_phone(phone: str) -> str:
    digits = ''.join(ch for ch in phone if ch.isdigit())
    if len(digits) < 10:
        raise ValueError('전화번호 짧음')
    return phone.strip()

def export_backup(path: str = 'projects/contacts_backup.json'):
    Path(path).write_text(json.dumps(load(), ensure_ascii=False, indent=2), encoding='utf-8')
    print('백업 저장', path)

def menu():
    while True:
        print('1 추가 2 검색 3 목록 4 삭제 5 백업 0 종료')
        choice = input('> ').strip()
        if choice == '0':
            break
        if choice == '1':
            name = input('이름: ').strip()
            if not name:
                print('이름 필요')
                continue
            phone = input('전화: ').strip()
            email = input('email(선택): ').strip()
            try:
                phone = normalize_phone(phone)
            except ValueError as err:
                print(err)
                continue
            add_contact(name, phone, email)
        elif choice == '2':
            key = input('검색: ').strip()
            found = search_contacts(key)
            if not found:
                print('결과 없음')
            for c in found:
                print(c)
        elif choice == '3':
            list_contacts()
        elif choice == '4':
            name = input('삭제할 이름: ').strip()
            delete_contact(name)
        elif choice == '5':
            export_backup()
        else:
            print('다시 선택')

if __name__ == '__main__':
    menu()
