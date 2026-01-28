from tabulate import tabulate

def display_arbs(arbs):
    if not arbs:
        print("No arbitrage opportunities found.")
        return
    
    table_data = []
    for arb in arbs:
        row = [
            arb["Team 1"],
            arb["Team 2"],
            f"{arb["Arbitrage %"]:.2f}%",
            arb["Bookie 1"],
            arb["Bookie 1 Odds"],
            arb["Bookie 2"],
            arb["Bookie 2 Odds"]
        ]
        table_data.append(row)

    headers = ["Team 1", "Team 2", "Arb %", "Bookie 1", "Odds", "Bookie 2", "Odds"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))