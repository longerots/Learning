import openmdao.api as om


class RectangleCompWithTags(om.ExplicitComponent):
    """
    A simple Explicit Component that also has input and output with tags.
    """
    def setup(self):
        self.add_input('length', val=1., tags=["tag1", "tag2"])
        self.add_input('width', val=1., tags=["tag2"])
        self.add_output('area', val=1., tags="tag1")

        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        outputs['area'] = inputs['length'] * inputs['width']


prob = om.Problem(RectangleCompWithTags())
prob.setup(check=False)
prob.run_model()

# Inputs no tags
inputs = prob.model.list_inputs(values=False, out_stream=None)
print(sorted(inputs))

# Input with tags
inputs = prob.model.list_inputs(values=False, out_stream=None, tags="tag1")
print(sorted(inputs))

# Input with multiple tags
inputs = prob.model.list_inputs(values=False, out_stream=None, tags=["tag1", "tag2"])
print(sorted(inputs))

# Inputs with tag that does not match
inputs = prob.model.list_inputs(values=False,out_stream=None, tags="tag3")
print(sorted(inputs))

# Outputs no tags
outputs = prob.model.list_outputs(values=False, out_stream=None)
print(sorted(outputs))

# Output with tags
outputs = prob.model.list_outputs(values=False, out_stream=None, tags="tag1")
print(sorted(outputs))

# Output with multiple tags
outputs = prob.model.list_outputs(values=False, out_stream=None, tags=['tag1', 'tag3'])
print(sorted(outputs))

# Outputs with tag that does not match
outputs = prob.model.list_outputs(values=False, out_stream=None, tags="tag3")
print(sorted(outputs))
