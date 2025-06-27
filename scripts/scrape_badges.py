import requests
from bs4 import BeautifulSoup

USERNAME = "deetechie27"
URL = f"https://tryhackme.com/p/{deetechie27}"

def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    badges = soup.find_all("img", {"class": "badges-icon"})

    with open("badges.md", "w") as f:
        f.write("## 🏅 TryHackMe Badges\n\n")
        for badge in badges:
            src = badge.get("src")
            alt = badge.get("alt", "Badge")
            full_url = f"https://tryhackme.com{src}"
            f.write(f'<img src="{full_url}" alt="{alt}" width="120"/>\n\n')

if __name__ == "__main__":
    main()
