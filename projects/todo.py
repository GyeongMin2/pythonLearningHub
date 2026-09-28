import json
from pathlib import Path

STORE = Path('projects/todos.json')

def load():
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text(encoding='utf-8'))

def save(items):
    STORE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')

def add_task(title):
    items = load()
    items.append({'title': title, 'done': False})
    save(items)

def toggle(title):
    items = load()
    for t in items:
        if t['title'] == title:
            t['done'] = not t['done']
    save(items)

def list_tasks():
    for t in load():
        mark = 'x' if t['done'] else ' '
        print(f'[{mark}] {t["title"]}')

if __name__ == '__main__':
    add_task('pandas 복습')
    list_tasks()

def menu():
    while True:
        print('1 add 2 toggle 3 list 0 quit')
        c = input('> ').strip()
        if c == '0':
            break
        if c == '1':
            add_task(input('title: ').strip())
        elif c == '2':
            toggle(input('title: ').strip())
        elif c == '3':
            list_tasks()
