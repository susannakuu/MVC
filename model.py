import helpers

class Model:
    def __init__(self, elemendid):
        self.lisa_elemendid(elemendid)

    def lisa_elemendid(self, elemendid):
        return helpers.lisa_elemendid(elemendid)

    def lisa_element(self, nimetus, hind, kogus):
        return helpers.lisa_element(nimetus, hind, kogus)

    def loe_elemendid(self):
        return helpers.loe_elemendid()

    def lisa_element(self, nimetus):
        return helpers.loe_element(nimetus)

    def uuenda_element(self, nimetus, hind, kogus):
        return helpers.uuenda_element(nimetus, hind, kogus)

    def kustuta_element(self, nimetus):
         helpers.kustuta_element(nimetus)

    def kustuta_elemendid(self):
         helpers.kustuta_elemendid()