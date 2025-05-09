import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sirv_model(y, t, beta, gamma, v_rate):
    S, I, R, V = y
    dS_dt = -beta * S * I - v_rate * S
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    dV_dt = v_rate * S
    return [dS_dt, dI_dt, dR_dt, dV_dt]

def run_simulation(species, beta=0.002, gamma=0.1, duration=160, resolution=500):
    t = np.linspace(0, duration, resolution)
    results = {}
    consolidated_df = pd.DataFrame()

    for sp_name, values in species.items():
        y0 = [values['S0'], values['I0'], 0, 0]
        sol = odeint(sirv_model, y0, t, args=(beta, gamma, values['v_rate']))
        results[sp_name] = sol

        S, I, R, V = sol.T
        temp_df = pd.DataFrame({
            "Time (days)": t,
            "Susceptible": S,
            "Infectious": I,
            "Recovered": R,
            "Vaccinated": V,
            "Species": sp_name
        })
        consolidated_df = pd.concat([consolidated_df, temp_df], ignore_index=True)

    return consolidated_df, results

def plot_results(results, t=None):
    if t is None:
        t = np.linspace(0, 160, 500)

    fig, axs = plt.subplots(len(results), 1, figsize=(10, 5 * len(results)))

    for idx, (sp_name, sol) in enumerate(results.items()):
        S, I, R, V = sol.T
        axs[idx].plot(t, S, label='Susceptible')
        axs[idx].plot(t, I, label='Infectious')
        axs[idx].plot(t, R, label='Recovered')
        axs[idx].plot(t, V, label='Vaccinated')
        axs[idx].set_title(f"{sp_name} - SIRV Model")
        axs[idx].set_xlabel("Time (days)")
        axs[idx].set_ylabel("Population")
        axs[idx].legend()
        axs[idx].grid(True)

    plt.tight_layout()
    plt.show()

def main():
    species = {
        'Humans': {'S0': 283_000_000, 'I0': 47_000_000, 'v_rate': 0.001},
        'Mallard Ducks': {'S0': 6_270_000, 'I0': 330_000, 'v_rate': 0.0005},
        'Yorkshire Pigs': {'S0': 65_700_000, 'I0': 7_300_000, 'v_rate': 0.0008}
    }

    df, results = run_simulation(species)
    df.to_csv("data/sirv_influenza_all_species.csv", index=False)
    plot_results(results)
    print("Simulation complete. CSV saved to data/sirv_influenza_all_species.csv")

if __name__ == "__main__":
    main()
