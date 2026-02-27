class Animal:
    def __init__(self, species, health):
        self.species = species
        self.health = health


# ---- Hierarchical traits ----
traits = {
    "respiratory_system": {
        "gills": {"temperature": 10, "humidity": 100, "elevation": 5, "terrestrial": 0, "aqueous": 100},
        "lungs": {"temperature": 15, "humidity": 50, "elevation": 50, "terrestrial": 75, "aqueous": 25},
        "tracheal_system": {"temperature": 35, "humidity": 40, "elevation": 10, "terrestrial": 100, "aqueous": 0},
        "cutaneous_respiration": {"temperature": 15, "humidity": 90, "elevation": 30, "terrestrial": 40, "aqueous": 60},
    },

    "blood_system": {
        "ectothermic": {"temperature": 32, "humidity": 70, "elevation": 20, "terrestrial": 60, "aqueous": 40},
        "endothermic": {"temperature": 5, "humidity": 50, "elevation": 70, "terrestrial": 85, "aqueous": 15},
    },

    "digestive_system": {
        "carnivorous": {"temperature": 10, "humidity": 50, "elevation": 60, "terrestrial": 80, "aqueous": 20},
        "herbivorous": {"temperature": 20, "humidity": 70, "elevation": 40, "terrestrial": 90, "aqueous": 10},
        "omnivorous": {"temperature": 15, "humidity": 55, "elevation": 50, "terrestrial": 70, "aqueous": 30},
    },

    "skeleton": {
        "bone_internal": {"temperature": 10, "humidity": 50, "elevation": 70, "terrestrial": 80, "aqueous": 20},
        "bone_exoskeleton": {"temperature": 30, "humidity": 40, "elevation": 20, "terrestrial": 100, "aqueous": 0},
        "cartilage": {"temperature": 12, "humidity": 100, "elevation": 5, "terrestrial": 0, "aqueous": 100},
        "none": {"temperature": 18, "humidity": 90, "elevation": 10, "terrestrial": 30, "aqueous": 70},
    },

    "skin": {
        "scales": {"temperature": 30, "humidity": 30, "elevation": 20, "terrestrial": 80, "aqueous": 20},
        "fur": {"temperature": 0, "humidity": 50, "elevation": 80, "terrestrial": 90, "aqueous": 10},
        "skin": {"temperature": 18, "humidity": 80, "elevation": 40, "terrestrial": 60, "aqueous": 40},
        "feathers": {"temperature": 5, "humidity": 50, "elevation": 70, "terrestrial": 70, "aqueous": 30},
    },

    "limbs_type": {
        "legs": {"temperature": 15, "humidity": 50, "elevation": 60, "terrestrial": 100, "aqueous": 0},
        "fins": {"temperature": 10, "humidity": 100, "elevation": 5, "terrestrial": 0, "aqueous": 100},
        "wings": {"temperature": 5, "humidity": 50, "elevation": 80, "terrestrial": 60, "aqueous": 40},
        "tentacles": {"temperature": 12, "humidity": 90, "elevation": 5, "terrestrial": 10, "aqueous": 90},
        "none": {"temperature": 18, "humidity": 85, "elevation": 15, "terrestrial": 40, "aqueous": 60},
    },

    "activity_cycle": {
        "diurnal": {"temperature": 20, "humidity": 50, "elevation": 50, "terrestrial": 70, "aqueous": 30},
        "nocturnal": {"temperature": 10, "humidity": 60, "elevation": 40, "terrestrial": 80, "aqueous": 20},
    },

    "body_size": {
        "tiny": {"temperature": 30, "humidity": 50, "elevation": 30, "terrestrial": 95, "aqueous": 5},
        "small": {"temperature": 25, "humidity": 60, "elevation": 40, "terrestrial": 70, "aqueous": 30},
        "medium": {"temperature": 15, "humidity": 55, "elevation": 50, "terrestrial": 75, "aqueous": 25},
        "large": {"temperature": 5, "humidity": 50, "elevation": 70, "terrestrial": 85, "aqueous": 15},
        "gigantic": {"temperature": 0, "humidity": 80, "elevation": 10, "terrestrial": 10, "aqueous": 90},
    }
}


# Normalization ranges
_ranges = {
    "temperature": (-20.0, 50.0),
    "humidity": (0.0, 100.0),
    "elevation": (0.0, 4000.0),
    "terrestrial": (0.0, 100.0),
    "aqueous": (0.0, 100.0),
}


def _norm(value, lo, hi):
    v = float(value)
    v = max(lo, min(hi, v))
    return (v - lo) / (hi - lo)


def trait_to_curve(trait_tuple):
    """
    Convert (category, trait_name) → normalized 5-point curve.
    """
    if not isinstance(trait_tuple, tuple) or len(trait_tuple) != 2:
        return []

    cat_name, trait_name = trait_tuple

    # match category (case-insensitive)
    category = next((c for c in traits if c.lower() == cat_name.lower()), None)
    if category is None:
        return []

    # match trait
    trait = next((t for t in traits[category] if t.lower() == trait_name.lower()), None)
    if trait is None:
        return []

    attrs = traits[category][trait]

    vec = [
        _norm(attrs["temperature"], *_ranges["temperature"]),
        _norm(attrs["humidity"], *_ranges["humidity"]),
        _norm(attrs["elevation"], *_ranges["elevation"]),
        _norm(attrs["terrestrial"], *_ranges["terrestrial"]),
        _norm(attrs["aqueous"], *_ranges["aqueous"]),
    ]

    # cumulative mean
    curve = []
    s = 0.0
    for i, v in enumerate(vec, start=1):
        s += v
        curve.append(s / i)

    return curve
