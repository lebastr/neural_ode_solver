import torch

def r(st):
    """ calculates a-b: a by rows, b by cols """
    cs = st[0]
    return torch.unsqueeze(cs,1) - cs

def make_F(masses):
    def F(state):
        nonlocal masses
        rs = r(state)
        dists = ((rs ** 2).sum(dim=2).sqrt() + torch.eye(rs.shape[0])).unsqueeze(dim=2)
        rd = rs / dists
        accs = rd.permute([2,0,1]) @ masses
        accs = -accs.permute([1,0])

        state2 = torch.stack([state[1], accs])
        return state2
    return F