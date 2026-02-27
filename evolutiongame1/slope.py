import numpy as np
import matplotlib.pyplot as plt

from class_animals import trait_to_curve
from class_habitat import habitat_to_curve


def _align_curve(curve, n):
    if not curve:
        return [0.0] * n
    if len(curve) >= n:
        return curve[:n]
    return curve + [curve[-1]] * (n - len(curve))


def _average_trait_curve(trait_tuples):
    curves = [trait_to_curve(t) for t in trait_tuples]
    curves = [c for c in curves if c]

    if not curves:
        return []

    max_len = max(len(c) for c in curves)
    aligned = [_align_curve(c, max_len) for c in curves]

    return np.mean(np.array(aligned), axis=0).tolist()


def render_slope_comparison(selected_traits, habitat_name):

    trait_curve = _average_trait_curve(selected_traits)
    habitat_curve = habitat_to_curve(habitat_name)

    if not trait_curve or not habitat_curve:
        print("Invalid curves.")
        return

    n = 5
    steps = list(range(1, 6))

    trait_curve = _align_curve(trait_curve, n)
    habitat_curve = _align_curve(habitat_curve, n)

    plt.figure("Compatibility of Traits and Habitat")
    plt.clf()

    labels = ["temperature", "humidity", "elevation", "terrestrial", "aqueous"]

    plt.plot(steps, trait_curve, marker="o", linewidth=2, color="blue", label="Your Animal Evolution")
    plt.plot(steps, habitat_curve, linestyle="--", color="green", label=f"{habitat_name} Ideal")

    plt.fill_between(steps, trait_curve, habitat_curve, alpha=0.1)

    plt.xticks(steps, labels, rotation=20)
    plt.ylim(0, 1)

    plt.xlabel("Habitat Factors")
    plt.ylabel("Normalized Adaptation Strength")
    plt.title(f"Trait–Habitat Compatibility ({habitat_name})")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.pause(0.1)
    plt.show(block=False)
