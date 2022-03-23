class IdentifiedObject:
    # Initializes an object with an OID (and sets current ID one higher)
    def __init__(self, oid):
        self._oid = oid

    @property
    def oid(self):
        return self._oid

    def __eq__(self, other):
        return self._oid == other.oid and self == other
         

    def __hash__(self):
        return hash(self._oid)

    






