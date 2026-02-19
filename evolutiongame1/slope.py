import numpy as np
from matplotlib import pyplot as plt
from class_animals import trait_to_curve as _trait_to_curve

def ideal_habitat_curve(curve: list[float], length: int) -> list[float]:
    """ The habitat curve is normalized to the same number of steps. Expand or shrink `curve` to match `length` points. Empty input yields a flat zero curve."""
    if length <= 0:
        return []
    if not curve:
        return [0.0] * length
    if len(curve) == length:
        return list(curve)

    x_old = np.linspace(0, 1, num=len(curve))
    x_new = np.linspace(0, 1, num=length)
    y_new = np.interp(x_new, x_old, np.array(curve, dtype=float))
    return y_new.tolist()

def _average_trait_curve(selected_traits: list) -> list[float]:
    """Average the cumulative-mean curves for the selected traits."""
    if not selected_traits:
        return []

    curves = [_trait_to_curve(t) for t in selected_traits]
    curves = [c for c in curves if c]  # drop unknown/empty

    if not curves:
        return []

    # All trait curves should be length 5 by design; still, align to be safe.
    max_len = max(len(c) for c in curves)
    curves = [c if len(c) == max_len else ideal_habitat_curve(c, max_len) for c in curves]
    return np.mean(np.array(curves, dtype=float), axis=0).tolist()

def render_slope_comparison(selected_traits: list[float], habitat_curve: list[float], habitat_name: str, center_for_visuals: bool = False, show_diff_shading: bool = True,) -> None:
    """Compares animal trait compatability with the habitat's ideal conditions. Average of all selected trait curves. Plot 2 slopes (trait vs habitat)."""
    # Build averaged trait curve using shared logic (no duplication).
    trait_curve = _average_trait_curve(selected_traits)

    # Pick a common number of steps and align both curves for plotting/comparison.
    n_steps = max(len(trait_curve), len(habitat_curve), 5)
    steps = list(range(1, n_steps + 1))

    trait_aligned = ideal_habitat_curve(trait_curve, n_steps)
    habitat_aligned = ideal_habitat_curve(habitat_curve, n_steps)

    # Compatibility
    mean_trait = float(np.mean(trait_curve)) if trait_curve else 0.0
    mean_hab = float(np.mean(habitat_aligned)) if habitat_aligned else 0.0
    diff = mean_trait - mean_hab
    verdict = "Good Fit" if abs(diff) <= 0.05 else "Bad Fit"

    # Plot
    plot_trait = np.array(trait_aligned, dtype=float)
    plot_habitat = np.array(habitat_aligned, dtype=float)
    if center_for_visuals:
        plot_trait = plot_trait - plot_trait.mean()
        plot_habitat = plot_habitat - plot_habitat.mean()

    plt.figure("Compatability of Traits and Habitat")
    plt.clf() # Clears the old graph
    if show_diff_shading:
        # Build piecewise shading based on which curve is on top
        plt.fill_between(
            steps, plot_trait, plot_habitat,
            where=(plot_trait >= plot_habitat),
            interpolate=True, color="#3498db", alpha=0.12, label="Trait above Habitat"
        )
        plt.fill_between(
            steps, plot_trait, plot_habitat,
            where=(plot_trait < plot_habitat),
            interpolate=True, color="#27ae60", alpha=0.12, label="Habitat above Trait"
        )

        # Lines and points
    plt.plot(steps, plot_trait, color="#3498db", marker="o", linewidth=3, label="Your Animal Evolution")
    plt.plot(steps, plot_habitat, color="#27ae60", linestyle="--", linewidth=2, label=f"{habitat_name} Ideal")

    # Text & axes
    title_suffix = " (centered)" if center_for_visuals else ""
    plt.title(f"Compatibility of Traits vs Habitat — {habitat_name}")
    plt.xlabel("Evolutionary Steps")
    plt.ylabel("Adaptation Strength" + (" (centered)" if center_for_visuals else ""))
    plt.grid(True, alpha=0.3)
    plt.legend(ncol=2)
    plt.xticks(steps)
    plt.xlim(min(steps) - 0.5, max(steps) + 0.5)

    # Verdict label (computed on non-centered aligned means)
    plt.gcf().text(0.02, 0.96, f"{verdict}", fontsize=9, va="top")

    plt.tight_layout()
    plt.pause(0.1)
    plt.show(block=False)




