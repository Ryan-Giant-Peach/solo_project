from db.run_sql import run_sql

from models.source import Source
from models.sound import Sound
import repositories.sound_repository as sound_repository

def save(source):
    sql = "INSERT INTO sources (items, no_items, sound_id) VALUES (%s, %s, %s) RETURNING *"
    values = [source.items, source.no_items, source.sound.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    source.id = id
    return source
