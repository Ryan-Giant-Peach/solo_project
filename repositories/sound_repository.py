from db.run_sql import run_sql
from models.source import Source
from models.sound import Sound

def save(sound):
    sql = "INSERT INTO sounds (sound_name, genre) VALUES (%s, %s) RETURNING *"
    values = [sound.sound_name, sound.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    sound.id = id
    return sound

def select_all():
    sounds = []

    sql = "SELECT * FROM sounds"
    results = run_sql(sql)

    for row in results:
        sound = Sound(row['sound_name'], row['genre'], row['id'] )
        sounds.append(sound)
    return sounds



def select(id):
    sound = None
    sql = "SELECT * FROM sounds WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        sound = Sound(result['sound_name'], result['genre'], result['id'] )
    return sound