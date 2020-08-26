import numpy as np
import openmdao.api as om


class VectorDoublingComp(om.ExplicitComponent):

    def initialize(self):
        self.options.declare('size', types=int)

    def setup(self):
        size = self.options['size']

        self.add_input('x', shape=size)
        self.add_output('y', shape=size)
        self.declare_partials('y', 'x', val=2.,
                              rows=np.arange(size),
                              cols=np.arange(size))

    def compute(self, inputs, outputs):
        outputs['y'] = 2 * inputs['x']


prob = om.Problem()
prob.model.add_subsystem('double', VectorDoublingComp())

try:
    prob.setup()

# prob.set_val('double.x', [1., 2., 5.])
#
# prob.run_model()
# print(prob.get_val('double.y'))
except RuntimeError as err:
    print(str(err))