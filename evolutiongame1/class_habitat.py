
class Habitat:
    def __init__(self, temperature, humidity, elevation, terrestrial, aqueous):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestrial = terrestrial
        self.aqueous = aqueous

#humidity goes from 0/100 and elevation/temperature and terrestrial/aqueous are 0/100 with respect to each other are real numbers
habitats = {
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
        "elevation": 0,
        "terrestrial": 0,
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
        "temperature": -10,
        "humidity": 60,
        "elevation": 3000,
        "terrestrial": 90,
        "aqueous": 10
    },
    "Lake": {
        "temperature": 10,
        "humidity": 100,
        "elevation": 0,
        "terrestrial": 0,
        "aqueous": 100
    },
    "Shore": {
        "temperature": 15,
        "humidity": 80,
        "elevation": 0,
        "terrestrial": 40,
        "aqueous": 60
    },
 }

_ranges = {
    "temperature": (-20.0, 50.0),  # °C
    "humidity":    (0.0,   100.0), # %
    "elevation":   (0.0,   4000.0),# meters
    "terrestrial": (0.0,   100.0), # %
    "aqueous":      (0.0,   100.0), # %
}

def _norm(value: float, lo: float, hi: float) -> float:
    # Clips the value into [lowest, highest] and scales it in the range [0, 1]
    v = float(value)
    if hi == lo:
        return 0.0
    v = max(lo, min(hi, v))
    return (v - lo) / (hi - lo)

def _habitat_to_dict(name: str, h: Habitat) -> dict:
    # Convert a Habitat object to a dictionary with raw attributes + a normalized curve
    attrs = {
        "temperature": getattr(h, "temperature", 0.0),
        "humidity":    getattr(h, "humidity", 0.0),
        "elevation":   getattr(h, "elevation", 0.0),
        "terrestrial": getattr(h, "terrestrial", 0.0),
        "aqueous":      getattr(h, "aqueous", 0.0),
    }

    # Normalize each attribute into [0,1]
    vec = [
        _norm(attrs["temperature"], *_ranges["temperature"]),
        _norm(attrs["humidity"],    *_ranges["humidity"]),
        _norm(attrs["elevation"],   *_ranges["elevation"]),
        _norm(attrs["terrestrial"], *_ranges["terrestrial"]),
        _norm(attrs["aqueous"],      *_ranges["aqueous"]),
    ]

    # Cumulative mean curve required for the slope.
    curve = []
    s = 0.0
    for i, v in enumerate(vec, start=1):
        s += v
        curve.append(s / i)

    return {
        "name": name,
        "attributes": attrs,  # raw, unscaled values, if you need to display them
        "curve": curve,       # 5-point list[float], scaled 0..1, cumulative mean
    }
