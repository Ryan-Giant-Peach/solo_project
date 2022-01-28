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


def select_all():
    sources = []

    sql = "SELECT * FROM sources"
    results = run_sql(sql)

    for row in results:
        sound = sound_repository.select(row['sound_id'])
        source = Source(row['items'], row['no_items'], sound, row['id'] )
        sources.append(source)
    return sources
    
def delete(id):
    sql = "DELETE  FROM sources WHERE id = %s"
    values = [id]
    run_sql(sql, values) 