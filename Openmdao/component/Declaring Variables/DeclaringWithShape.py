import openmdao.api as om


class CompAddWithShape(om.ExplicitComponent):
    """Component for tests for declaring only shape."""

    def setup(self):
        self.add_input('x_a', shape=2)
        self.add_input('x_b', shape=(2, 2))
        self.add_input('x_c', shape=[2, 2])

        self.add_output('y_a', shape=3)
        self.add_output('y_b', shape=(3, 3))
        self.add_output('y_c', shape=[3, 3])


p = om.Problem(model=CompAddWithShape())
p.setup()

print(p.get_val('x_a'))
print(p.get_val('x_b'))
print(p.get_val('x_c'))
print(p.get_val('y_a'))
print(p.get_val('y_b'))
print(p.get_val('y_c'))