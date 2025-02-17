import numpy as np

class KalmanFilter:
    def __init__(self, x0, P0, A, B, C, Q, R):
        self.x = x0
        self.P = P0
        self.A = A
        self.B = B
        self.C = C
        self.Q = Q
        self.R = R

    def predict(self, u):
        self.x = self.A @ self.x + self.B @ u
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z):
        K = self.P @ self.C.T @ np.linalg.inv(self.C @ self.P @ self.C.T + self.R)
        self.x = self.x + K @ (z - self.C @ self.x)
        self.P = self.P - K @ self.C @ self.P

    def step(self, u, z):
        self.predict(u)
        self.update(z)