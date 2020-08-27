"""
Declaring with only the default value
"""
import openmdao.api as om
import numpy as np


class CompAddWithDefault(om.ExplicitComponent):
    """component for tests for declaring only default value."""

    def setup(self):
        self.add_input('x_a')
        self.add_input('x_b', val=3.)
        self.add_input('x_c', val=(3., 3.))
        self.add_input('x_d', val=[3., 3.])
        self.add_input('x_e', val=3. * np.ones((2, 2)))

        self.add_output('y_a')
        self.add_output('y_b', val=6.)
        self.add_output('y_c', val=(6., 6., 6.))
        self.add_output('y_d', val=[6., 6., 6.])
        self.add_output('y_e', val=6. * np.ones((3, 2)))


p = om.Problem(model=CompAddWithDefault())
p.setup()

print('x_a=', p.get_val('x_a'))
print('x_b=', p.get_val('x_b'))
print('x_c=', p.get_val('x_c'))
print('x_d=', p.get_val('x_d'))
print('x_e=', p.get_val('x_e'))
print('y_a=', p.get_val('y_a'))
print('y_b=', p.get_val('y_b'))
print('y_c=', p.get_val('y_c'))
print('y_d=', p.get_val('y_d'))
print('y_e=', p.get_val('y_e'))
