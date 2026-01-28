from typing import List, Dict, Optional
from difflib import SequenceMatcher

def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_arbitrage(odds_a: float, odds_b: float) -> Optional[float]:
    net_prob = (1 / odds_a) + (1 / odds_b)
    if net_prob < 1:
        return round((1 - net_prob) * 100, 2)
    return None

def split_teams(event):
    try: 
        team1, team2 = event["teams"].split(" vs ")
        return team1.strip(), team2.strip()
    except ValueError:
        return None

def identify_arbs(events1: List[Dict], events2: List[Dict]) -> List[Dict]:
    arbs = []

    for event_a in events1:
        team1_a, team2_a = split_teams(event_a)
        if not team1_a:
            continue
        for event_b in events2:
            team1_b, team2_b = split_teams(event_b)
            if not team1_b:
                continue
            if similar(team1_a, team1_b) >= 0.9 and similar(team2_a, team2_b) >= 0.9:
                bookie1_team1 = event_a["odds"][0]
                bookie2_team2 = event_b["odds"][1]
                arb_percent1 = find_arbitrage(bookie1_team1, bookie2_team2)
                if arb_percent1:
                    arbs.append({
                        "Team 1": team1_a,
                        "Team 2": team2_a,
                        "Arbitrage %": arb_percent1,
                        "Bookie 1": event_a["bookie"],
                        "Bookie 1 Odds": bookie1_team1,
                        "Bookie 2": event_b["bookie"],
                        "Bookie 2 Odds": bookie2_team2,
                    })

                bookie1_team2 = event_a["odds"][1]
                bookie2_team1 = event_b["odds"][0]
                arb_percent2 = find_arbitrage(bookie1_team2, bookie2_team1)
                if arb_percent2:
                    arbs.append({
                        "Team 1": team1_a,
                        "Team 2": team2_a,
                        "Arbitrage %": arb_percent2,
                        "Bookie 1": event_a["bookie"],
                        "Bookie 1 Odds": bookie1_team2,
                        "Bookie 2": event_b["bookie"],
                        "Bookie 2 Odds": bookie2_team1,
                    })

    return arbs
