class Animal:  # parent class
    def __init__(self, species, health):
        self.species = species
        self.health = health

class terrestial(Animal):  # subclass 1):
    def __init__(self, species, health, lungs, fur, colour, limbs):
        super().__init__(species, health)
        self.lungs = lungs
        self.fur = fur
        self.colour = colour
        self.limbs = limbs


class aquatic(Animal):  # subclass 2)
    def __init__(self, species, health, gills, fins, scales):
        super().__init__(species, health)
        self.gills = gills
        self.fins = fins
        self.scales = scales



class Trait:
    def __init__(self, temperature: float, humidity: float, elevation: float,
                 terrestrial: float, aqueous: float):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestrial = terrestrial
        self.aqueous = aqueous

# Raw trait attributes (same 5 fields as habitats)
traits: dict[str, dict[str, float]] = {
    "Fur": {
        "temperature": -5,
        "humidity": 40,
        "elevation": 500,
        "terrestrial": 90,
        "aqueous": 10
    },
    "Climbing": {
        "temperature": 15,
        "humidity": 50,
        "elevation": 800,
        "terrestrial": 85,
        "aqueous": 15
    },
    "Burrowing": {
        "temperature": 30,
        "humidity": 20,
        "elevation": 50,
        "terrestrial": 95,
        "aqueous": 5
    },
    "Speed": {
        "temperature": 25,
        "humidity": 40,
        "elevation": 200,
        "terrestrial": 100,
        "aqueous": 0
    },
    "Swimming": {
        "temperature": 12,
        "humidity": 90,
        "elevation": 0,
        "terrestrial": 20,
        "aqueous": 80
    },
    "Gills": {
        "temperature": 8,
        "humidity": 95,
        "elevation": 0,
        "terrestrial": 0,
        "aqueous": 100
    },
    "Camouflage": {
        "temperature": 15,
        "humidity": 60,
        "elevation": 300,
        "terrestrial": 80,
        "aqueous": 20
    },
}

# ---- Same normalization ranges you used for habitats ----
_ranges = {
    "temperature": (-20.0, 50.0),
    "humidity":    (0.0,   100.0),
    "elevation":   (0.0,   4000.0),
    "terrestrial": (0.0,   100.0),
    "aqueous":     (0.0,   100.0),
}

def _norm(value: float, lo: float, hi: float) -> float:
    v = float(value)
    if hi == lo:
        return 0.0
    v = max(lo, min(hi, v))
    return (v - lo) / (hi - lo)

def trait_to_curve_from_attrs(attrs: dict[str, float]) -> list[float]:
    """Convert the raw trait attributes into normalized 5-point cumulative-mean curve (0..1), matching the habitat curve construction."""
    t = {
        "temperature": attrs.get("temperature", 0.0),
        "humidity":    attrs.get("humidity", 0.0),
        "elevation":   attrs.get("elevation", 0.0),
        "terrestrial": attrs.get("terrestrial", 0.0),
        "aqueous":     attrs.get("aqueous", 0.0),
    }
    vec = [
        _norm(t["temperature"], *_ranges["temperature"]),
        _norm(t["humidity"],    *_ranges["humidity"]),
        _norm(t["elevation"],   *_ranges["elevation"]),
        _norm(t["terrestrial"], *_ranges["terrestrial"]),
        _norm(t["aqueous"],     *_ranges["aqueous"]),
    ]

    #Cumulative mean curve required for the slope.
    curve, s = [], 0.0
    for i, v in enumerate(vec, start=1):
        s += v
        curve.append(s / i)
    return curve

def trait_to_curve(trait_name: str) -> list[float]:
    """Case-insensitive lookup by name, then build the curve."""
    if trait_name in traits:
        return trait_to_curve_from_attrs(traits[trait_name])

    low = trait_name.lower()
    for k, v in traits.items():
        if k.lower() == low:
            return trait_to_curve_from_attrs(v)

    return []  # unknown trait
