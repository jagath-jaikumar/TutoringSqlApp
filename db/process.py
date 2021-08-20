import json

import db.models as models


def persist_simple_table(simple_object, session):
    """Persist an app with metadata"""
    simple_model = models.SimpleTable(name=simple_object.name)

    session.add(simple_model)
    session.flush()

    return True
