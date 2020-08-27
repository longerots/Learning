import openmdao.api as om
# from ModelUsingParaboloid import Paraboloid
from openmdao.test_suite.components.paraboloid import Paraboloid

prob = om.Problem()
model = prob.model

model.add_subsystem('comp', Paraboloid(), promotes=['x', 'y', 'f_xy'])

prob.setup()

prob.set_val('x', 2.)
prob.set_val('y', 10.)
prob.run_model()
print(prob.get_val('f_xy'))

prob.set_val('x', 0.)
prob.set_val('y', 0.)
prob.run_model()
print(prob.get_val('f_xy'))

prob.set_val('x', 4.)
prob.set_val('y', 8.)
prob.run_model()
print(prob.get_val('f_xy'))

