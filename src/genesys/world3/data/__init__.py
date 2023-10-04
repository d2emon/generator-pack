from db import NestedModel
from genesys.nested.models import models


universe = NestedModel(
    models.Universe()
).save()
supercluster = NestedModel(
    models.Supercluster(),
    parent=universe,
).save()
galaxy = NestedModel(
    models.Galaxy(),
    parent=supercluster,
).save()
