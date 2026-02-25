import numpy as np
from matplotlib import pyplot as plt
from class_animals import trait_to_curve as _trait_to_curve
from class_habitat import habitat_to_curve as _habitat_curve_from_name


# -------------------------------------------------
# Curve alignment helper
# -------------------------------------------------
def _align_curve(curve, n: int):
    """Pad or trim a curve to exactly n values."""
    if not curve:
        return [0.0] * n
    if len(curve) == n:
        return curve
    if len(curve) > n:
        return curve[:n]
    return curve + [curve[-1]] * (n - len(curve))


# -------------------------------------------------
# Averaging trait curves (multiple trait names → 1 curve)
# -------------------------------------------------
def _average_trait_curve(selected_traits: list) -> list[float]:
    """
    Takes a list of trait identifiers (names/keys expected by class_animals.trait_to_curve)
    and returns the mean curve across them.
    """
    if not selected_traits:
        return []

    # Convert names → curve data
    curves = [_trait_to_curve(t) for t in selected_traits]
    curves = [c for c in curves if c]

    if not curves:
        return []

    max_len = max(len(c) for c in curves)
    aligned = [_align_curve(c, max_len) for c in curves]

    return np.mean(np.array(aligned, float), axis=0).tolist()


# -------------------------------------------------
# PLOT FUNCTION
# -------------------------------------------------
def render_slope_comparison(
    selected_traits: list,
    habitat_name: str,
    center_for_visuals: bool = False,
    show_diff_shading: bool = True,
):
    """
    Plot the averaged trait curve vs. the habitat curve.
    Habitat curve comes from `habitat_to_curve` (already fixed).
    """

    # Compute the trait curve (average of selected traits)
    trait_curve = _average_trait_curve(selected_traits)

    # Fetch habitat curve (this is now a list[float], length 5)
    habitat_curve = _habitat_curve_from_name(habitat_name)

    # If either is missing, don't crash
    if not trait_curve or not habitat_curve:
        print("Invalid trait or habitat curve.")
        return

    # Determine plotting length
    n_steps = max(len(trait_curve), len(habitat_curve), 5)
    steps = list(range(1, n_steps + 1))

    # ✔ Correct: simply align the curves, do NOT re‑average them
    trait_aligned = _align_curve(trait_curve, n_steps)
    habitat_aligned = _align_curve(habitat_curve, n_steps)

    # Compute compatibility
    mean_trait = float(np.mean(trait_curve))
    mean_hab = float(np.mean(habitat_curve))
    diff = mean_trait - mean_hab
    verdict = "Good Fit" if abs(diff) <= 0.05 else "Bad Fit"

    # Convert to numpy for shading operations
    plot_trait = np.array(trait_aligned, float)
    plot_habitat = np.array(habitat_aligned, float)

    # Optional centering
    if center_for_visuals:
        plot_trait -= plot_trait.mean()
        plot_habitat -= plot_habitat.mean()

    # ------------- Plotting ---------------
    plt.figure("Compatibility of Traits and Habitat")
    plt.clf()

    if show_diff_shading:
        # Shade where trait is above habitat
        plt.fill_between(
            steps, plot_trait, plot_habitat,
            where=(plot_trait >= plot_habitat),
            interpolate=True, alpha=0.12, color="#3498db"
        )
        # Shade where habitat is above trait
        plt.fill_between(
            steps, plot_trait, plot_habitat,
            where=(plot_trait < plot_habitat),
            interpolate=True, alpha=0.12, color="#27ae60"
        )

    # Actual curves
    plt.plot(
        steps, plot_trait, color="#3498db",
        marker="o", linewidth=3, label="Your Animal Evolution"
    )
    plt.plot(
        steps, plot_habitat, color="#27ae60",
        linestyle="--", linewidth=2, label=f"{habitat_name} Ideal"
    )

    # Titles / labels
    suffix = " (centered)" if center_for_visuals else ""
    plt.title(f"Compatibility of Traits vs Habitat — {habitat_name}{suffix}")
    plt.xlabel("Evolutionary Steps")
    plt.ylabel("Adaptation Strength" + suffix)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(steps)
    plt.xlim(min(steps) - 0.5, max(steps) + 0.5)

    # Verdict text
    plt.gcf().text(0.02, 0.96, verdict, fontsize=9, va="top")

    plt.tight_layout()
    plt.pause(0.1)
    plt.show(block=False)
