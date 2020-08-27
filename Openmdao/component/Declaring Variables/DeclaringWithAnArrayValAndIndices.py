"""Test declaring with array val and array indices."""
import openmdao.api as om
import numpy as np


class ComAddWithArrayIndices(om.ExplicitComponent):
    """Component for tests for declaring with array val and array indices."""

    def setup(self):
        self.add_input('x_a', val=2.0 * np.ones(6), src_indices=np.arange(6))
        # The shape must match
        self.add_input('x_b', val=2.0 * np.ones((3, 2)), src_indices=np.arange(6).reshape((3, 2)))

        self.add_output('y')


p = om.Problem(model=ComAddWithArrayIndices())
p.setup()

print(p.get_val('x_a'))
print(p.get_val('x_b'))