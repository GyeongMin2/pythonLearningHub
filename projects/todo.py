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
