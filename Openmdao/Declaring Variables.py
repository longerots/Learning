import openmdao.api as om
# class TestExplComSimple(om.ExplicitComponent)
from openmdao.api import ExplicitComponent


class TestExplCompSimple(ExplicitComponent):

    def setup(self):
        self.add_input('length', val=1., desc='length of rectangle')
        self.add_input('width', val=1., desc='width of rectangle')
        self.add_output('area', val=1., desc='area of rectangle')

        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        outputs['area'] = inputs['length'] * inputs['width']
