from make_data import run_all         
from plot import plot_all         


if __name__ == "__main__":
    df = run_all()
    df.to_csv("results.csv", index=False, encoding="utf-8-sig")
    
    plot_all(df)