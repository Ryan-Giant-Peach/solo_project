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

@sources_blueprint.route("/sources/<id>/delete", methods=['POST'])
def delete_source(id):
    source_repository.delete(id)
    return redirect('/sources')


# CREATE
@sources_blueprint.route("/sources", methods=['POST'])
def create_source():
    items = request.form['items']
    no_items = request.form['no_items']
    duration = request.form['duration']
    completed = request.form['completed']
    user = user_repository.select(user_id)
    task = Task(description, user, duration, completed)
    task_repository.save(task)
    return redirect('/tasks')