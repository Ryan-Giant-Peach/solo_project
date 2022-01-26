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