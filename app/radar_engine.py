import numpy as np
import matplotlib.pyplot as plt

def generate_radar(criteria, entities):
    labels = criteria
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)

    for name, values in entities.items():
        values = values + values[:1]
        ax.plot(angles, values, linewidth=2, label=name)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])

    plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.savefig("radar_output.png", dpi=300, bbox_inches="tight")
    plt.close()

    return "radar_output.png"
