"""
A component that computes y = func(x), where func is a function given as an option
"""
import openmdao.api as om
from types import FunctionType


class UnitaryFunctionComp(om.ExplicitComponent):
    def initialize(self):
        self.options.declare('func', types=FunctionType, recordable=False)

    def setup(self):
        self.add_input('x')
        self.add_output('y')
        self.declare_partials('y', 'x', method='fd')

    def compute(self, inputs, outputs):
        func = self.options['func']
        outputs['y'] = func(inputs['x'])


def my_func(x):
    return x*2


prob = om.Problem()
prob.model.add_subsystem('f_comp', UnitaryFunctionComp(func=my_func))

prob.setup()

prob.set_val('f_comp.x', 5.)

prob.run_model()
print(prob.get_val('f_comp.y'))
