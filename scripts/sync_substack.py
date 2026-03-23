#!/usr/bin/env python3
"""
Sync Substack RSS feed into Hugo external-link posts.

Each post becomes content/blog/<slug>.md with externalUrl pointing
back to Substack. No content is imported — just metadata.
"""

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import math

import feedparser

WORDS_PER_MINUTE = 200
CONTENT_DIR = Path(os.environ.get("CONTENT_DIR", "content/blog"))
RSS_URL = os.environ.get(
    "SUBSTACK_RSS_URL", "https://hdadhich01.substack.com/feed"
)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    segment = path.split("/")[-1] if path else ""
    return segment or slugify(url)


def parse_date(entry) -> datetime:
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    if hasattr(entry, "updated_parsed") and entry.updated_parsed:
        return datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def estimate_word_count(entry) -> int:
    """Extract plain text word count from RSS content or summary."""
    html = ""
    if hasattr(entry, "content") and entry.content:
        html = entry.content[0].get("value", "")
    if not html and hasattr(entry, "summary"):
        html = entry.summary or ""
    plain = re.sub(r"<[^>]+>", " ", html)
    words = plain.split()
    return len(words)


def build_post(entry, pub_date: datetime, substack_url: str) -> str:
    title = entry.get("title", "Untitled").replace('"', '\\"')
    description = entry.get("summary", "")
    if description:
        description = re.sub(r"<[^>]+>", "", description).strip()
        if len(description) > 200:
            description = description[:197] + "..."
        description = description.replace('"', '\\"')

    word_count = estimate_word_count(entry)
    reading_time = max(1, math.ceil(word_count / WORDS_PER_MINUTE))

    lines = [
        "---",
        f'title: "{title}"',
        f"date: {pub_date.strftime('%Y-%m-%d')}",
    ]
    if description:
        lines.append(f'description: "{description}"')
    lines += [
        f'externalUrl: "{substack_url}"',
        "showReadingTime: true",
        "build:",
        '  render: "never"',
        '  list: "local"',
        "---",
        "",
    ]

    filler = " ".join(["word"] * word_count)
    lines.append(f'<div style="display:none">{filler}</div>')
    lines.append("")

    return "\n".join(lines)


def sync_entry(entry) -> bool:
    substack_url = entry.get("link", "")
    slug = slug_from_url(substack_url) or slugify(entry.get("title", "untitled"))
    pub_date = parse_date(entry)

    post_path = CONTENT_DIR / f"{slug}.md"

    if post_path.exists():
        existing = post_path.read_text(encoding="utf-8")
        date_match = re.search(r"^date:\s*(\S+)", existing, re.MULTILINE)
        if date_match:
            try:
                old_date = datetime.strptime(date_match.group(1), "%Y-%m-%d").replace(
                    tzinfo=timezone.utc
                )
                if old_date >= pub_date:
                    print(f"  [skip] {slug}")
                    return False
            except ValueError:
                pass

    content = build_post(entry, pub_date, substack_url)
    post_path.write_text(content, encoding="utf-8")

    print(f"  [synced] {slug}")
    return True


def main():
    if not RSS_URL:
        print("ERROR: SUBSTACK_RSS_URL is not set.")
        sys.exit(1)

    print(f"Fetching: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)

    if feed.bozo and not feed.entries:
        print(f"ERROR: Failed to parse feed: {feed.bozo_exception}")
        sys.exit(1)

    print(f"Found {len(feed.entries)} entries.\n")
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    changed = 0
    for entry in feed.entries:
        try:
            if sync_entry(entry):
                changed += 1
        except Exception as exc:
            print(f"  [error] {entry.get('title', '?')}: {exc}")

    print(f"\nDone. {changed} post(s) synced.")


if __name__ == "__main__":
    raise SystemExit(main())
