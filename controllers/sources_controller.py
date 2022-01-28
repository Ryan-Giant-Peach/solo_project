from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import source_repository
from repositories import sound_repository
from models.source import Source

sources_blueprint = Blueprint("sources", __name__)

@sources_blueprint.route("/sources")
def sources():
    sources = source_repository.select_all()
    return render_template("sources/index.html", all_sources = sources)

@sources_blueprint.route("/sources/<id>", methods=['GET'])
def show_sources(id):
    source = source_repository.select(id)
    return render_template("sources/show.html", source = source)

@sources_blueprint.route("/sources/new", methods=['GET'])
def new_source():
    sounds = sound_repository.select_all()
    return render_template("sources/new.html", all_sounds = sounds)

@sources_blueprint.route("/sources/<id>/delete", methods=['POST'])
def delete_source(id):
    source_repository.delete(id)
    return redirect('/sources')

# CREATE
@sources_blueprint.route("/sources", methods=['POST'])
def create_source():
    items = request.form['items']
    no_items = request.form['no_items']
    sound = sound_repository.select(sound_id)
    source = Source(items, no_items)
    source_repository.save(source)
    return redirect('/sources')

# EDIT
# GET
@sources_blueprint.route('/sources/<id>/edit', methods=['GET'])
def edit_source(id):
    source = source_repository.select(id)
    sounds = sound_repository.select_all()
    return render_template('sources/edit.html', source = source, all_sounds = sounds)


# Update
# PUT '/sources/<id>'
@sources_blueprint.route("/sources/<id>", methods=['POST'])
def update_sources(id):
    items = request.form['items']
    no_items = request.form['no_items']
    sound_id = request.form['sound_id']
    sound = sound_repository.select(sound_id)
    source = Source(items, no_items, sound, id)
    source_repository.update(source)
    return redirect('/sources')
