from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import source_repository
from repositories import sound_repository
from models.source import Source
from models.sound import Sound

sounds_blueprint = Blueprint("sounds", __name__)


@sounds_blueprint.route("/sources", methods=['POST'])
def create_sound():
    items = request.form['items']
    no_items = request.form['no_items']
    sound_name = request.form['sound_name']
    genre = request.form['genre']
    sound = Sound(sound_name, genre)
    sound_repository.save(sound)
    source = Source(items, no_items, sound)
    source_repository.save(source)
    return redirect('/sources')

# @sources_blueprint.route("/sources", methods=['POST'])
# def create_source():
#     items = request.form['items']
#     no_items = request.form['no_items']
#     sound_id = request.form['sound_id']
#     sound = sound_repository.select(sound_id)
#     source = Source(items, no_items, sound)
#     source_repository.save(source)
#     return redirect('/sources')