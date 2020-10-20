#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    compartments: numeric, optional
        number of peripheral compartments

    """
    def __init__(self, compartments=0):
        if compartments < 0:
            raise ValueError("cannot have a negative number of compartments")
        self._compartments = compartments

    def get_compartments(self):
        return self._compartments

