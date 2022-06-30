from this import s
from entity import Entity

class Investment(Entity):
    def __unicode__(self):
        return {
            "name": self.name,
            "owner": self.owner
        }


