import matplotlib.pyplot as plt

def render_tree(selected_traits: list[str], habitat_name: str) -> None:
    """Builds the evolution tree automatically after each evolution."""
    steps = list(range(1, len(selected_traits) + 1))
    plt.figure("Trait Evolution Tree")
    plt.clf()

    # If there are no traits yet, show an empty scaffold
    if not steps:
        plt.title(f"Trait Evolution Tree — Habitat: {habitat_name}")
        plt.xlabel("Evolutionary Step")
        plt.ylabel("Trait")
        plt.text(0.5, 0.5, "No traits selected yet.", ha="center", va="center", transform=plt.gca().transAxes)
        plt.grid(True, alpha=0.3)
        plt.pause(0.1) # Small pause that allows the window to render
        plt.show(block=False) # Keeps the game running
        return

    # Plot points and labels
    y = [1] * len(steps)  # Constant row - just annotating names in order
    plt.scatter(steps, y, color="#3498db")


    for i, trait in enumerate(selected_traits, start=1):
        plt.annotate(trait, (i, 1), textcoords="offset points", xytext=(0, 10), ha="center")
    plt.plot(steps, y, color="#34495e", linewidth=2, zorder=2)  # connecting the points
    plt.yticks([])  # Hide y-axis ticks as this is a timeline
    plt.title(f"Trait Evolution Tree — Habitat: {habitat_name}")
    plt.xlabel("Evolutionary Step")
    plt.grid(True, axis="x", alpha=0.3)
    plt.xticks(steps)  # Force integer ticks
    plt.xlim(min(steps) - 0.5, max(steps) + 0.5)  # Prevent auto-zoom issues
    plt.tight_layout()
    plt.pause(0.1)
    plt.show(block=False)

