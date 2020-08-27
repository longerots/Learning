import openmdao.api as om
import numpy as np


class ComAddWithIndices(om.ExplicitComponent):
    """Component for tests for declaring only indices."""

    def setup(self):
        self.add_input('x_a', src_indices=0)
        self.add_input('x_b', src_indices=(0, 1))
        self.add_input('x_c', src_indices=[0, 1])
        self.add_input('x_d', src_indices=np.arange(6))
        self.add_input('x_e', src_indices=np.arange(6).reshape((3, 2)), shape=(3, 2))

        self.add_output('y')


p = om.Problem(model=ComAddWithIndices())
p.setup()

print(p.get_val('x_a'))
print(p.get_val('x_b'))
print(p.get_val('x_c'))
print(p.get_val('x_d'))
print(p.get_val('x_e'))