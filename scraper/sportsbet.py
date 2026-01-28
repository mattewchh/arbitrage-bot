from scraper.base import get_driver, wait_for_element, human_sleep, scroll_down
from bs4 import BeautifulSoup

def scrape_sportsbet():
    driver = get_driver()
    URL = "https://www.sportsbet.com.au/betting/darts"
    driver.get(URL)

    wait_for_element(driver, ".priceButton_f1n4s149") #adjust selector later

    for _ in range(5):
        scroll_down(driver, 600)

    human_sleep(1,2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract events
    events = []
    for event_div in soup.select("div.card_fohmrj3[data-automation-id$='-competition-event-card']"):
        first_team = event_div.select_one("span[data-automation-id$='-participant-1']")
        second_team = event_div.select_one("span[data-automation-id$='-participant-2']")
        
        teams = f"{first_team.text.strip()} vs {second_team.text.strip()}"

        odds_elements = event_div.select("span[data-automation-id$='-two-outcome-captioned-text']")
        odds = []
        for odd in odds_elements:
            try:
                odds.append(float(odd.text.strip()))
            except ValueError:
                continue
        
        events.append({
            "bookie": "Sportsbet",
            "teams": teams,
            "odds": odds
        })
    
    return events