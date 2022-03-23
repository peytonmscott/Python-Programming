from numpy import true_divide


class ObjectID:

    def __init__(self, oid):
       self.oid = oid

    def __eq__(self, oid1, oid2):
        if oid1 == oid2:
            return True
        else:
            return False
    
    def __hash__(self):
        pass


    






