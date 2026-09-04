#!/usr/bin/env python3
"""Odswieza kafelki najnowszych filmow z kanalu YouTube EcoHeat w index.html.

Zrodlo: publiczny kanal RSS YouTube (bez klucza API, bez limitow).
Podmieniany jest wylacznie fragment miedzy znacznikami YT:START / YT:END.
Uruchamiane codziennie przez .github/workflows/youtube.yml
"""
import html
import os
import re
import subprocess
import sys

CHANNEL_ID = "UCHyJ3fICqTuySy0P5NYYx1w"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
HOW_MANY = 3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "index.html")
START, END = "<!-- YT:START -->", "<!-- YT:END -->"


def fetch(url: str) -> str:
    out = subprocess.run(
        ["curl", "-sSL", "--max-time", "30", "-A", "Mozilla/5.0", url],
        capture_output=True, check=True,
    )
    return out.stdout.decode("utf-8", "replace")


def newest_videos(xml: str):
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    videos = []
    for e in entries[:HOW_MANY]:
        vid = re.search(r"<yt:videoId>([^<]+)</yt:videoId>", e)
        title = re.search(r"<title>(.*?)</title>", e, re.S)
        if not (vid and title):
            continue
        videos.append((vid.group(1), html.unescape(title.group(1)).strip()))
    return videos


def render(videos) -> str:
    cards = []
    for vid, title in videos:
        safe = html.escape(title, quote=True)
        cards.append(
            f'      <button class="yt-card" type="button" data-id="{vid}" '
            f'data-title="{safe}" aria-label="Odtwórz film: {safe}">\n'
            f'        <span class="yt-thumb">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" '
            f'width="480" height="360" loading="lazy" decoding="async">'
            f'<span class="yt-play" aria-hidden="true"></span></span>\n'
            f'        <span class="yt-name">{safe}</span>\n'
            f'      </button>'
        )
    return "\n".join(cards)


def main() -> int:
    videos = newest_videos(fetch(FEED))
    if not videos:
        print("Brak filmow w kanale RSS — nic nie zmieniam.", file=sys.stderr)
        return 1

    page = open(PAGE, encoding="utf-8").read()
    if START not in page or END not in page:
        print("Brak znacznikow YT:START / YT:END w index.html", file=sys.stderr)
        return 1

    before, rest = page.split(START, 1)
    _, after = rest.split(END, 1)
    updated = f"{before}{START}\n{render(videos)}\n{END}{after}"

    if updated == page:
        print("Bez zmian.")
        return 0

    open(PAGE, "w", encoding="utf-8").write(updated)
    print("Zaktualizowano filmy:")
    for vid, title in videos:
        print(f"  {vid}  {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
