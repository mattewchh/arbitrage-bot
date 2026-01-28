# Sports Arbitrage Bot

A Python bot that scrapes odds from **Sportsbet** and **Ladbrokes** and identifies potential sports betting arbitrage opportunities for match betting (e.g., Team A vs Team B).  
> For educational purposes only. Does not place bets.

## Features
- Scrapes live odds from Sportsbet and Ladbrokes  
- Detects two-way arbitrage opportunities in two outcomed match betting
- Calculates implied probability and potential profit margin  
- Terminal output using Python tabulate

## Tech Stack
- Python
- Selenium  
- BeautifulSoup4
- Tabulate  

## Installation
```bash
git clone https://github.com/your-username/arbitrage-bot.git
cd arbitrage-bot
pip install -r requirements.txt

```
## Usage
- Choose the sport you want to scrape by replacing the url(s) in scraper/ladbrokes.py and scraper/sportsbet.py
- To run the bot:

```bash
python main.py

```

