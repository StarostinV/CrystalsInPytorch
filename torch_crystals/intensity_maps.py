import torch
from torch import Tensor


class IntensityPolarMap(object):
    def __init__(self, size: tuple = (512, 512), device: torch.device = 'cuda', dtype: torch.dtype = torch.float64):
        self.size = size
        self.device = device
        self.dtype = dtype
        self.x = torch.arange(self.size[1], device=device, dtype=dtype)[None, :, None]
        self.y = torch.arange(self.size[0], device=device, dtype=dtype)[:, None, None]

    def generate_map(self, q_mod: Tensor, q_angle: Tensor, widths: Tensor, a_widths: Tensor, intensities: Tensor):
        if isinstance(widths, (float, int)):
            widths = torch.ones_like(q_mod) * widths
        if isinstance(a_widths, (float, int)):
            a_widths = torch.ones_like(q_mod) * a_widths
        return generate_polar_map(self.x, self.y, q_mod, q_angle, widths, a_widths, intensities)


@torch.jit.script
def generate_polar_map(x: Tensor, y: Tensor,
                       q_mod: Tensor, q_angle: Tensor, widths: Tensor, a_widths: Tensor,
                       intensities: Tensor):
    return (intensities[None, None] * (
        torch.exp(
            - torch.abs(x - q_mod[None, None]) ** 2 / widths[None, None] ** 2 / 2
            - (y - q_angle[None, None]) ** 2 / a_widths[None, None] ** 2 / 2
        )
    )).sum(-1)
