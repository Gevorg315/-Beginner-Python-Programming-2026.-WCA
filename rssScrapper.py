import argparse
import html
import json as json_mod
import sys
from typing import Optional, Sequence, Any
import xml.etree.ElementTree as ET
import urllib.request

class RSSReaderError(Exception):
    """Base exception."""

class ParseError(RSSReaderError):
    """Raised when the XML document is malformed."""

def clean_text(text: Optional[str]) -> Optional[str]:
    """Clean string data to resolve HTML-encoding artifacts like &#39;."""
    if text is None:
        return None
    return html.unescape(text.strip())

def get_all_tags(element: ET.Element, tag_name: str) -> list[str]:
    """Retrieve all occurrences of a specific tag inside an element."""
    found_tags = []
    for child in element.findall(tag_name):
        cleaned = clean_text(child.text)
        if cleaned:
            found_tags.append(cleaned)
    return found_tags

def format_console(data: dict) -> list[str]:
    """Format the parsed RSS dictionary data into exact console output lines."""
    lines = []
    channel_mappings = [
        ("title", "Feed"),
        ("link", "Link"),
        ("lastBuildDate", "Last Build Date"),
        ("pubDate", "Publish Date"),
        ("language", "Language"),
        ("categories", "Categories"),
        ("managingEditor", "Editor"),
        ("description", "Description")
    ]
    for key, label in channel_mappings:
        val = data.get(key)
        if not val:
            continue
        if key == "categories":
            lines.append(f"{label}: {', '.join(val)}")
        else:
            lines.append(f"{label}: {val}")
    if data["items"]:
        lines.append("")  # Space between channel elements and items
    item_mappings = [
        ("title", "Title"),
        ("author", "Author"),
        ("pubDate", "Published"),
        ("link", "Link"),
        ("categories", "Categories")
    ]
    for item in data["items"]:
        for key, label in item_mappings:
            val = item.get(key)
            if not val:
                continue
            if key == "categories":
                lines.append(f"{label}: {', '.join(val)}")
            else:
                lines.append(f"{label}: {val}")
        if item.get("description"):
            lines.append(f"\n{item['description']}")
        lines.append("")  # Trailing spacing gap separating feed elements
    return lines

def format_json(data: dict) -> list[str]:
    """Format the parsed RSS dictionary data into a clean JSON string list."""
    cleaned_json_data = {}
    for key in ["title", "link", "description", "lastBuildDate", "pubDate", "language", "managingEditor"]:
        if data.get(key):
            cleaned_json_data[key] = data[key]
    if data.get("categories"):
        cleaned_json_data["category"] = data["categories"]
    # FIX: Only append the "items" array if there are items to populate
    if data.get("items"):
        cleaned_json_data["items"] = []
        for item in data["items"]:
            cleaned_item = {}
            for key in ["title", "author", "pubDate", "link", "description"]:
                if item.get(key):
                    cleaned_item[key] = item[key]
            if item.get("categories"):
                cleaned_item["category"] = item["categories"]
            cleaned_json_data["items"].append(cleaned_item)
    # Return as a single-element list containing the full pretty-printed JSON string
    return [json_mod.dumps(cleaned_json_data, indent=2, ensure_ascii=False)]

def rss_parser(xml_content: str, limit: Optional[int] = None, use_json: bool = False, json_output: bool = False,
               json: bool = False) -> list[str] | str:
    """Parse specifications from RSS 2.0 matching your assertions exactly."""
    should_use_json = use_json or json_output or json
    try:
        root = ET.fromstring(xml_content.strip())
    except ET.ParseError as e:
        raise ParseError(f"Provided source text is not valid XML: {e}")
    channel = root.find("channel")
    if channel is None:
        raise ParseError("Invalid RSS format: <channel> element not found.")
    feed_data: dict[str, Any] = {
        "title": clean_text(channel.findtext("title")),
        "link": clean_text(channel.findtext("link")),
        "lastBuildDate": clean_text(channel.findtext("lastBuildDate")),
        "pubDate": clean_text(channel.findtext("pubDate")),
        "language": clean_text(channel.findtext("language")),
        "categories": get_all_tags(channel, "category"),
        "managingEditor": clean_text(channel.findtext("managingEditor")),
        "description": clean_text(channel.findtext("description")),
        "items": []
    }
    item_nodes = channel.findall("item")
    if limit is not None and limit > 0:
        item_nodes = item_nodes[:limit]
    for item in item_nodes:
        item_data = {
            "title": clean_text(item.findtext("title")),
            "author": clean_text(item.findtext("author")),
            "pubDate": clean_text(item.findtext("pubDate")),
            "link": clean_text(item.findtext("link")),
            "categories": get_all_tags(item, "category"),
            "description": clean_text(item.findtext("description"))
        }
        feed_data["items"].append(item_data)
    if should_use_json:
        # We take the JSON string element directly out of format_json's list
        return [format_json(feed_data)[0]]
    return format_console(feed_data)

def test_rss_parser():
    """Explicit test container un-indented so PyCharm and Python can reach it."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
        <channel>
            <title>Example RSS Feed</title>
            <link>https://www.nasa.gov/news-release/feed/</link>
            <description>An example RSS feed.</description>
            <language>en-us</language>
            <lastBuildDate>Tue, 28 Sep 2021 00:00:00 GMT</lastBuildDate>
            <pubDate>Tue, 28 Sep 2021 00:00:00 GMT</pubDate>
            <category>News</category>
            <category>Technology</category>
            <managingEditor>editor@example.com</managingEditor>
            <item>
                <title>Article 1</title>
                <link>https://www.example.com/article1.html</link>
                <description>Article 1 description.</description>
                <category>News</category>
                <category>Technology</category>
                <pubDate>Tue, 28 Sep 2021 00:00:00 GMT</pubDate>
                <author>author1@example.com</author>
            </item>
            <item>
                <title>Article 2</title>
                <link>https://www.example.com/article2.html</link>
                <description>Article 2 description.</description>
                <category>News</category>
                <category>Sports</category>
                <pubDate>Tue, 28 Sep 2021 00:00:00 GMT</pubDate>
                <author>author2@example.com</author>
            </item>
        </channel>
    </rss>
    """
    expected_output = [
        "Feed: Example RSS Feed",
        "Link: https://www.nasa.gov/news-release/feed/",
        "Last Build Date: Tue, 28 Sep 2021 00:00:00 GMT",
        "Publish Date: Tue, 28 Sep 2021 00:00:00 GMT",
        "Language: en-us",
        "Categories: News, Technology",
        "Editor: editor@example.com",
        "Description: An example RSS feed.",
        "",
        "Title: Article 1",
        "Author: author1@example.com",
        "Published: Tue, 28 Sep 2021 00:00:00 GMT",
        "Link: https://www.example.com/article1.html",
        "Categories: News, Technology",
        "\nArticle 1 description.",
        "",
        "Title: Article 2",
        "Author: author2@example.com",
        "Published: Tue, 28 Sep 2021 00:00:00 GMT",
        "Link: https://www.example.com/article2.html",
        "Categories: News, Sports",
        "\nArticle 2 description.",
        ""
    ]
    assert rss_parser(xml, limit=None, json_output=False) == expected_output
    assert rss_parser(xml, limit=1, json_output=False) == expected_output[:16]
    json_res = json_mod.loads(rss_parser(xml, limit=None, json_output=True)[0])
    assert json_res["title"] == "Example RSS Feed"
    assert len(json_res["items"]) == 2
    print("All tests passed successfully!")

def main(argv: Optional[Sequence] = None):
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    parser.add_argument("source", type=str, help="RSS URL")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--limit", type=int, default=None, help="Limit news topics")
    args = parser.parse_args(argv)
    try:
        with urllib.request.urlopen(args.source) as response:
            xml = response.read().decode("utf-8")
        print("\n".join(rss_parser(xml, args.limit, args.json)))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # If you run the file directly without arguments, you can trigger your test runner:
    if len(sys.argv) == 1:
        test_rss_parser()
    else:
        main()
