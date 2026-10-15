import numpy as np

class FlowIntegrator:
    def __init__(self, step_h: float, threshold: float):
        self.h = h
        self.threshold = threshold

    def integrate(self, pressure_sign: np.darray) -> float:
        if len(pressure_sign) < 2:
            return 0.0

        anomaly = np.clip(pressure_sign - self.threshold, a_min = 0, a_max = None)
        midpoints = (anomaly[:-1] + anomaly[1:]) / 2.0

        area = self.h * np.sum(midpoints)
        return float(area)

