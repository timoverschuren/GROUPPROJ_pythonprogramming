import matplotlib.pyplot as plt

def render_tree(selected_traits, habitat_name):
    plt.figure("Trait Evolution Tree")
    plt.clf()

    steps = list(range(1, len(selected_traits) + 1))
    y = [1] * len(steps)

    if not steps:
        plt.title(f"Trait Evolution Tree — Habitat: {habitat_name}")
        plt.text(0.5, 0.5, "No traits selected", ha="center", transform=plt.gca().transAxes)
        plt.show(block=False)
        return

    plt.scatter(steps, y, color="blue")

    # label each trait
    for i, (cat, trait) in enumerate(selected_traits, start=1):
        text = f"{cat}:{trait}"
        plt.annotate(text, (i, 1), xytext=(0, 10), textcoords="offset points", ha="center")

    plt.plot(steps, y, color="black")
    plt.yticks([])

    plt.title(f"Trait Evolution Tree — Habitat: {habitat_name}")
    plt.xlabel("Evolution Steps")
    plt.grid(True, axis="x", alpha=0.3)
    plt.xticks(steps)
    plt.xlim(0.5, len(steps) + 0.5)

    plt.tight_layout()
    plt.pause(0.1)
    plt.show(block=False)
