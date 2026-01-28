from arbitrage.arb_checker import identify_arbs
from scraper.ladbrokes import scrape_ladbrokes
from scraper.sportsbet import scrape_sportsbet
from display.tabulate import display_arbs

ladbrokes_events = scrape_ladbrokes()
sportsbet_events = scrape_sportsbet()

arbs = identify_arbs(ladbrokes_events, sportsbet_events)
display_arbs(arbs)