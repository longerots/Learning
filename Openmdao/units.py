import openmdao.api as om


class SpeedComp(om.ExplicitComponent):
    """Simple speed computation from distance and time with unit conversations."""

    def setup(self):
        self.add_input('distance', val=1.0, units='km')
        self.add_input('time', val=1.0, units='h')
        self.add_output('speed', val=1.0, units='km/h')

    def compute(self, inputs, outputs):
        outputs['speed'] = inputs['distance'] / inputs['time']


prob = om.Problem()
prob.model.add_subsystem('c1', SpeedComp())
prob.model.add_subsystem('c2', om.ExecComp('f=speed', speed={'units':'m/s'}))

prob.model.set_input_defaults('c1.distance', val=1., units='m')
prob.model.set_input_defaults('c1.time', val=1., units='s')

prob.model.connect('c1.speed', 'c2.speed')  # 此处的 connect 只可以从ouput 连接到input， 不能从input 连接 input

prob.setup()
prob.run_model()

print(prob.get_val('c1.distance'))
print(prob.get_val('c1.time'))
print(prob.get_val('c1.speed'))
print(prob.get_val('c2.f'))
