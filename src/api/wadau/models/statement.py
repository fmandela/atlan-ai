from investor import Investor

class Statement(Investor):
    def __unicode__(self):
        return "Investment summary"
