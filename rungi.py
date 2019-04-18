
class Rungi:
    def __init__(self, dyn, state, h=None):
        self.dyn = dyn
        self.state = state
        self.h = h

    def step(self, h=None):
        if h is None:
            h = self.h

        k1 = h * self.dyn(self.state)
        k2 = h * self.dyn(self.state + k1 / 2)
        k3 = h * self.dyn(self.state + k2 / 2)
        k4 = h * self.dyn(self.state + k3)

        new_state = self.state + (k1 + 2*k2 + 2*k3 + k4) / 6
        old_state = self.state
        self.state = new_state
        return old_state, new_state

