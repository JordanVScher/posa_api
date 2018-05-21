"""creating database

Revision ID: fa986520fd32
Revises: 
Create Date: 2018-05-20 21:11:21.356101

"""
from alembic import op
import sqlalchemy as sa
from db_conn import conn

# revision identifiers, used by Alembic.
revision = 'fa986520fd32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn.execute("create database posa_db;")
    # updated engines on db_conn and alimbic.ini to include the name of the database


def downgrade():
    conn.execute("drop database if exists posa_db;")
