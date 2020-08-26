import openmdao.api as om


class ScalingExample2(om.ImplicitComponent):
    def setup(self):
        self.add_input('x1', val=100.0)
        self.add_input('x2', val=5000.0)
        self.add_output('y1', val=200., ref=300.0, ref0=100.0)
        self.add_output('y2', val=6000., ref=11000.0, ref0=1000.0)

    def apply_nonlinear(self, inputs, outputs, residuals, discrete_inputs=None,
                        discrete_outputs=None):
        x1 = inputs['x1']
        x2 = inputs['x2']
        y1 = outputs['y1']
        y2 = outputs['y2']

        residuals['y1'] = 1e5 * (x1 - y1) / y1
        residuals['y2'] = 1e-5 * (x2 - y2) / y2


prob = om.Problem(model=ScalingExample2())

prob.setup()

print(prob.get_val('y1'))
print(prob.get_val('y2'))
