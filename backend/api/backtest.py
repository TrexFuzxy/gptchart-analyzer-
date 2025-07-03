import pandas as pd
from io import StringIO

def run_backtest(file, entry_price, stop_loss, take_profit):
    df = pd.read_csv(file)
    wins, losses = 0, 0

    for _, row in df.iterrows():
        if row['low'] <= stop_loss:
            losses += 1
        elif row['high'] >= take_profit:
            wins += 1

    total = wins + losses
    winrate = (wins / total * 100) if total > 0 else 0
    return {"total": total, "wins": wins, "losses": losses, "winrate": round(winrate, 2)}