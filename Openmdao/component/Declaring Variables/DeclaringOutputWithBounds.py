"""Test declaring bounds."""
import openmdao.api as om
import numpy as np


class ComAddWithBounds(om.ExplicitComponent):
    """Component for tests for declaring bounds."""

    def setup(self):
        self.add_input('x')

        self.add_output('y_a', val=2.0, lower=2.)
        self.add_output('y_b', val=2.0, lower=0., upper=10.)
        self.add_output('y_c', val=2.0 * np.ones(6), lower=np.zeros(6), upper=10.)
        self.add_output('y_d', val=2.0 * np.ones(6), lower=0., upper=[12, 10, 10, 10, 10, 12])
        self.add_output('y_e', val=2.0 * np.ones((3, 2)), lower=np.zeros((3, 2)))


p = om.Problem(model=ComAddWithBounds())
p.setup()

print(p.get_val('y_a'))
print(p.get_val('y_b'))
print(p.get_val('y_c'))
print(p.get_val('y_d'))
print(p.get_val('y_e'))