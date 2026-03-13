
class Habitat:
    # Base class for habitats, with attributes that define the conditions of the habitat
    def __init__(self, temperature, humidity, elevation, terrestrial, aqueous):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestrial = terrestrial
        self.aqueous = aqueous


# humidity goes 0..100; elevation/temperature and terrestrial/aqueous are real numbers.
habitats = {
    # Each habitat has specific attributes that define its conditions and suitability for different species
    "Desert": {
        "temperature": 40,
        "humidity": 10,
        "elevation": 20,
        "terrestrial": 99,
        "aqueous": 1
    },
    "Ocean": {
        "temperature": 10,
        "humidity": 100,
        "elevation": 1,
        "terrestrial": 1,
        "aqueous": 100
    },
    "Forest": {
        "temperature": 15,
        "humidity": 40,
        "elevation": 100,
        "terrestrial": 75,
        "aqueous": 25
    },
    "Mountains": {
        "temperature": 1,
        "humidity": 60,
        "elevation": 100,
        "terrestrial": 90,
        "aqueous": 10
    },
    "Lake": {
        "temperature": 10,
        "humidity": 100,
        "elevation": 1,
        "terrestrial": 1,
        "aqueous": 100
    },
    "Shore": {
        "temperature": 15,
        "humidity": 80,
        "elevation": 1,
        "terrestrial": 40,
        "aqueous": 60
    },
}

_ranges = {
    # Normalization ranges for habitat attributes, used to scale raw values into a 0-1 range for comparison and visualization
    "temperature": (0.0,   50.0),   # °C
    "humidity":    (0.0,   100.0),  # %
    "elevation":   (0.0,   100.0), # meters
    "terrestrial": (0.0,   100.0),  # %
    "aqueous":     (0.0,   100.0),  # %
}


def _norm(value: float, lo: float, hi: float) -> float:
    """Clip value to [lo, hi] and scale to [0, 1]."""
    v = float(value)
    if hi == lo:
        return 0.0
    v = max(lo, min(hi, v))
    return (v - lo) / (hi - lo)


def _habitat_to_dict(name: str, h: Habitat) -> dict:
    """
    Convert a Habitat object to a dictionary with raw attributes and a normalized
    5-point cumulative-mean curve (values in [0,1]).
    """
    attrs = {
        "temperature": getattr(h, "temperature", 0.0),
        "humidity":    getattr(h, "humidity", 0.0),
        "elevation":   getattr(h, "elevation", 0.0),
        "terrestrial": getattr(h, "terrestrial", 0.0),
        "aqueous":     getattr(h, "aqueous", 0.0),
    }

    # Normalize each attribute into [0,1]
    vec = [
        _norm(attrs["temperature"], *_ranges["temperature"]),
        _norm(attrs["humidity"],    *_ranges["humidity"]),
        _norm(attrs["elevation"],   *_ranges["elevation"]),
        _norm(attrs["terrestrial"], *_ranges["terrestrial"]),
        _norm(attrs["aqueous"],     *_ranges["aqueous"]),
    ]

    # Cumulative mean curve required for the slope

    curve = vec[:]  # Use raw normalized 5 factors

    return {
        "name": name,
        "attributes": attrs,  # raw, unscaled values
        "curve": curve,       # list[float], length 5
    }


def habitat_to_curve(habitat_name: str) -> list[float]:
    """
    Case-insensitive lookup by name, build the Habitat object,
    and return ONLY the 5-point cumulative-mean curve.
    """
    # exact match
    profile = habitats.get(habitat_name)

    # case-insensitive fallback
    if profile is None:
        low = habitat_name.lower()
        for k, v in habitats.items():
            if k.lower() == low:
                profile = v
                habitat_name = k  # normalize case
                break

    if profile is None:
        return []  # unknown habitat

    h = Habitat(
        temperature=profile["temperature"],
        humidity=profile["humidity"],
        elevation=profile["elevation"],
        terrestrial=profile["terrestrial"],
        aqueous=profile["aqueous"],
    )

    return _habitat_to_dict(habitat_name, h)["curve"]


# (Optional) helpers if you want UI labels/tooltips
def habitat_profile(habitat_name: str) -> dict:
    """
    Return the full dict with name, raw attributes, and curve.
    Useful for debugging or UI display.
    """
    # exact match
    profile = habitats.get(habitat_name)

    # case-insensitive fallback
    if profile is None:
        low = habitat_name.lower()
        for k, v in habitats.items():
            if k.lower() == low:
                profile = v
                habitat_name = k
                break

    if profile is None:
        return {}

    h = Habitat(
        temperature=profile["temperature"],
        humidity=profile["humidity"],
        elevation=profile["elevation"],
        terrestrial=profile["terrestrial"],
        aqueous=profile["aqueous"],
    )

    return _habitat_to_dict(habitat_name, h)
