#!/usr/bin/env python3

import csv
import os
import random
import string
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

# This script take a Letterboxd user as an input or an argument, download the rss file with all the movies that the user have previously reviewed.
# Then it turns the RSS file XML content, turn it into a CSV file and integrate it to prompt in a markdownfile.
# All of that to allows the AI to make a "preferences profile" aboute the user.


def generate_random_filename():
    """Generate a random filename with uppercase letters and numbers"""
    return (
        "".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + ".rss"
    )


def download_rss(username):
    """Download the RSS file from Letterboxd"""
    url = f"https://letterboxd.com/{username}/rss/"
    filename = generate_random_filename()

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
    )

    try:
        with urllib.request.urlopen(req) as response:
            with open(filename, "wb") as out_file:
                out_file.write(response.read())
        return filename
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found on Letterboxd.")
        else:
            print(
                f"Error: Failed to download RSS feed. HTTP Error {e.code}: {e.reason}"
            )
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)


def xml_to_csv(xml_file, csv_file):
    """Convert XML data to CSV format"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    namespaces = {"letterboxd": "https://letterboxd.com"}

    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Film Title", "Rating"])

        for item in root.findall(".//item"):
            film_title = item.find("letterboxd:filmTitle", namespaces=namespaces)
            member_rating = item.find("letterboxd:memberRating", namespaces=namespaces)

            csv_writer.writerow(
                [
                    film_title.text if film_title is not None else "",
                    member_rating.text if member_rating is not None else "",
                ]
            )


def generate_markdown(username, csv_content):
    """Generate a markdown file with the prompt and CSV content"""
    markdown_content = f"""# Movie Preference Analysis Task

## Input
Analyze the following CSV containing a user's watched movie history. The CSV includes the columns: `Film Title` and `Rating`.

## Objective
1. **Estimate the user's age range** based on the release years of the watched movies and their ratings.
2. **Calculate genre preferences** as a normalized score (0 to 1) for each of the following genres:
   - Action
   - Adventure
   - Animation
   - Biography
   - Comedy
   - Crime
   - Documentary
   - Drama
   - Family
   - Fantasy
   - History
   - Horror
   - Musical
   - Mystery
   - Romance
   - Sci-Fi (Science Fiction)
   - Sport
   - Thriller
   - War
   - Western

3. **Identify the top 4 most appreciated genres** based on the highest scores.
4. **Output only the JSON** in the following format:

{{
  "profile": {{
    "age_range": [min_age, max_age],
    "genres": {{
      "Action": score,
      "Adventure": score,
      "Animation": score,
      "Biography": score,
      "Comedy": score,
      "Crime": score,
      "Documentary": score,
      "Drama": score,
      "Family": score,
      "Fantasy": score,
      "History": score,
      "Horror": score,
      "Musical": score,
      "Mystery": score,
      "Romance": score,
      "Sci-Fi": score,
      "Sport": score,
      "Thriller": score,
      "War": score,
      "Western": score
    }},
    "top_genres": [
      "Genre1",
      "Genre2",
      "Genre3",
      "Genre4"
    ]
  }}
}}

Here is the CSV:

```csv
{csv_content}
```
"""

    with open(f"{username}.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(markdown_content)


def run_profile_prompter(username):
    """Run the entire profile prompter pipeline and return the markdown content"""
    rss_file = download_rss(username)
    csv_file = f"{username}.csv"

    xml_to_csv(rss_file, csv_file)

    with open(csv_file, "r", encoding="utf-8") as csvfile:
        csv_content = csvfile.read()

    markdown_content = create_markdown(username, csv_content)

    if rss_file:
        os.remove(rss_file)
    if os.path.exists(csv_file):
        os.remove(csv_file)

    return markdown_content


def create_markdown(username, csv_content):
    """Generate a markdown file with the prompt and CSV content"""
    markdown_content = f"""# Movie Preference Analysis Task

## Input
Analyze the following CSV containing a user's watched movie history. The CSV includes the columns: `Film Title` and `Rating`.

## Objective
1. **Estimate the user's age range** based on the release years of the watched movies and their ratings.
2. **Calculate genre preferences** as a normalized score (0 to 1) for each of the following genres:
   - Action
   - Adventure
   - Animation
   - Biography
   - Comedy
   - Crime
   - Documentary
   - Drama
   - Family
   - Fantasy
   - History
   - Horror
   - Musical
   - Mystery
   - Romance
   - Sci-Fi (Science Fiction)
   - Sport
   - Thriller
   - War
   - Western

3. **Identify the top 4 most appreciated genres** based on the highest scores.
4. **Output only the JSON** in the following format:

{{
  "profile": {{
    "age_range": [min_age, max_age],
    "genres": {{
      "Action": score,
      "Adventure": score,
      "Animation": score,
      "Biography": score,
      "Comedy": score,
      "Crime": score,
      "Documentary": score,
      "Drama": score,
      "Family": score,
      "Fantasy": score,
      "History": score,
      "Horror": score,
      "Musical": score,
      "Mystery": score,
      "Romance": score,
      "Sci-Fi": score,
      "Sport": score,
      "Thriller": score,
      "War": score,
      "Western": score
    }},
    "top_genres": [
      "Genre1",
      "Genre2",
      "Genre3",
      "Genre4"
    ]
  }}
}}

Here is the CSV:

```csv
{csv_content}
```
"""

    os.makedirs("cache/prompt", exist_ok=True)
    with open(f"cache/prompt/{username}.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(markdown_content)

    return markdown_content


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter the Letterboxd username: ")

    run_profile_prompter(username)
