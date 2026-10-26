import matplotlib.pyplot as plt

def plot_all(df):
    exp = {
    "identical_size": ("n", "Размер N (M = N)", "M = N"),
    "fixed_m": ("n", "Размер N при M = 100", "M = 100, N растёт"),
    "varying_ratio": ("ratio", "Отношение N/M при N = 2^20", "N = 2^20, N/M растёт")
    }
    
    for name, df_ in df.groupby("experiment", sort=False):
        exp_name = exp[name]
        
        for alg_name, alg_df in df_.groupby("algorithm"):
            plt.plot(alg_df[exp_name[0]], alg_df["time"], ".-", label=alg_name)
        plt.xscale("log", base=2)          
        plt.yscale("log", base=2)
        plt.xlabel(exp_name[1])
        plt.ylabel("Время, секунды")
        plt.title(exp_name[2])
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.savefig(f"graph_{name}.png", dpi=150)
        plt.show()