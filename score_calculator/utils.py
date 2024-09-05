def extract(x, dimension):
    """Extract dimensions/questions from SF-12 vector.

    Returns:
        The extracted value corresponding to the dimension/question.
    """

    if isinstance(x, dict): 

        if dimension not in [f"Q{i}" for i in range(1, 13)]:

        return x.get(dimension)  # Attempt to get the value, might return None if key doesn't exist
    else:
        raise ValueError(f"Unknown SF-12 question: {dimension}")

def coalesce(a, b):
    return a if a is not None else b

def recode(value, *zvalue):
    return zvalue[value - 1]