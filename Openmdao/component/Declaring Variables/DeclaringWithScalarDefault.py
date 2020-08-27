"""Test declaring a scalar val with an array variable"""
import openmdao.api as om
import numpy as np


class CompAddArrayWithScalar(om.ExplicitComponent):
    """Component for tests for declaring a scalar val with an array variable."""

    def setup(self):
        self.add_input('x_a', val=2.0, shape=6)
        self.add_input('x_b', val=2.0, shape=(3, 2))
        self.add_input('x_c', val=2.0, src_indices=np.arange(6))
        self.add_input('x_d', val=2.0, src_indices=np.arange(6).reshape((3, 2)), shape=(3, 2))

        self.add_output('y_a', val=3.0, shape=6)
        self.add_output('y_b', val=3.0, shape=(3, 2))


p = om.Problem(model=CompAddArrayWithScalar())
p.setup()

print(p.get_val('x_a'))
print(p.get_val('x_b'))
print(p.get_val('x_c'))
print(p.get_val('x_d'))