"""Adjust or add rules to evaluate combinations of work factors here."""


class PointsRules:
    """Evaluate the combimation of simple and complex work factors to return a point estimate.

    Attributes
    ----------
    simple: int
        Number of simple work factors.
    complex: int
        Number of complex work factors.
    valid: bool
        Check that both simple and complex are non-zero, non-negative.

    Methods
    -------
    check_valid(simple, complex)
        Returns True if args are both non-zero, non-negative ints.

    one()
        Returns 1 if conditions are met.

    three()
        Returns 3 if conditions are met.

    five()
        Returns 5 if conditions are met.

    estimate()
        Runs one(), three(), and five() to return a point estimate.

    Returns
    -------
    est: int
        The estimated point value. False if none of the points conditions apply.
    too_many_points: bool
        True if the work factors would produce an estimate higher than 5.
    """

    def __init__(self, simple, complex):
        self.simple = simple
        self.complex = complex
        self.valid = self.check_valid(simple, complex)
        self.est = None
        self.too_many_points = None

    @staticmethod
    def check_valid(simple, complex):
        """Returns True if args are both non-zero, non-negative ints."""
        if not simple and not complex:
            raise Exception("Invalid Parameters")
        elif not isinstance(simple, int) and not isinstance(complex, int):
            raise Exception("Invalid Parameters")
        elif simple < 0 or complex < 0:
            raise Exception("Invalid Parameters")
        else:
            return True

    def one(self):
        """Returns 1 if conditions are met."""
        if self.valid is False:
            return self
        elif self.simple and self.complex:
            return False
        elif self.simple and not self.complex:
            s_min, s_max = 1, 3
            c_min, c_max = 0, 0
        elif self.complex and not self.simple:
            return False
        self.est = (
            1
            if s_min <= self.simple <= s_max and c_min <= self.complex <= c_max
            else False
        )

    def three(self):
        """Returns 3 is conditions are met."""
        if self.est:
            return self
        elif self.simple and self.complex:
            s_min, s_max = 1, 3
            c_min, c_max = 1, 1
        elif self.simple and not self.complex:
            s_min, s_max = 4, 5
            c_min, c_max = 0, 0
        elif self.complex and not self.simple:
            s_min, s_max = 0, 0
            c_min, c_max = 1, 2

        self.est = (
            3
            if s_min <= self.simple <= s_max and c_min <= self.complex <= c_max
            else False
        )

    def five(self):
        """Returns 5 if conditions are met."""
        if self.est:
            return self.est
        elif self.simple and self.complex:
            s_min, s_max = 3, 5
            c_min, c_max = 2, 2
        elif self.simple and not self.complex:
            s_min, s_max = 5, 7
            c_min, c_max = 0, 0
        elif self.complex and not self.simple:
            s_min, s_max = 0, 0
            c_min, c_max = 3, 4

        self.est = (
            5
            if s_min <= self.simple <= s_max and c_min <= self.complex <= c_max
            else False
        )

    def estimate(self):
        """Runs one(), three(), and five() to return a point estimate."""
        for point_est in [self.one, self.three, self.five]:
            point_est()
        self.too_many_points = True if self.est is False else False
        return self
