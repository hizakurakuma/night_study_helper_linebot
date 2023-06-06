from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()