import openmdao.api as om
from openmdao.test_suite.components.sellar import SellarDerivatives

prob = om.Problem(model=SellarDerivatives())
prob.model.nonlinear_solver = om.NonlinearBlockGS()

prob.setup()

prob.set_val('x', 2.75)

prob.run_model()
print(prob.get_val('y1'))