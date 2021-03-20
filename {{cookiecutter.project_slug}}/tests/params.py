from collections import Counter

rules_params = [
    ("1. 1, 1 returns 3", 1, 1, 3, False),
    ("2. 0, 1 returns 3", 0, 1, 3, False),
    ("3. 1,0 returns 1", 1, 0, 1, False),
    ("4. 3, 0 returns 3", 3, 0, 1, False),
    ("5. 0, 2 returns 3", 0, 2, 3, False),
    ("6. 3, 2 returns 5", 3, 2, 5, False),
    ("7. 3, 1 returns 5", 3, 1, 3, False),
    ("8. 3, 4 returns too_many_points", 3, 4, False, True),
    ("9. 0, 2 returns 3", 0, 2, 3, False),
    ("10. 4, 0 returns 3", 4, 0, 3, False),
    ("11. 6, 0 returns 5", 6, 0, 5, False),
    ("12. 0, 3 returns 5", 0, 3, 5, False),
]
rules_ids = [x[0] for x in rules_params]

rules_invalid = [
    ("1. 0,0 raises exception", 0, 0, False),
    ("2. None input raises exception", None, None, False),
    ("3. Negative numbers raises exception", -1, -2, False),
    ("4. Non-integer input raises exception", "a", "b", False),
]
invalid_ids = [x[0] for x in rules_invalid]

profile_params = [
    (
        "1. Valid options and work factors",
        ["type1"],
        {
            "simple": 2,
            "complex": 1,
            "counts": Counter({"simple": 2, "A": 1, "B": 1, "complex": 1, "E": 1}),
        },
    )
]
profile_ids = [x[0] for x in profile_params]

estimate_points = [
    (
        "1. Valid profile input succeeds",
        (2, 1, Counter({"simple": 2, "A": 1, "B": 1, "complex": 1, "E": 1})),
        3,
        {"E", "A", "B"},
    ),
    (
        "2. Invalid options and work factors",
        (
            4,
            4,
            Counter(
                {
                    "simple": 4,
                    "A": 1,
                    "B": 1,
                    "C": 1,
                    "H": 1,
                    "complex": 4,
                    "E": 1,
                    "D": 1,
                    "F": 1,
                    "G": 1,
                }
            ),
        ),
        False,
        {"A", "B", "C", "H", "E", "D", "F", "G"},
    ),
]
estimate_points_ids = [x[0] for x in estimate_points]
