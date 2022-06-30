class Entity:
    def __init__(self, id, name, description, type, created_at, updated_at, units, owner):
        self.id = id
        self.name = name 
        self.description = description 
        self.type = type 
        self.created_at = created_at
        self.updated_at = updated_at
        self.units = units 
        self.owner = owner
    
    def __unicode__(self):
        return "Investment entity"