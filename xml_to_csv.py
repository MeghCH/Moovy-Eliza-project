#!/usr/bin/env python3

import csv
import sys
import xml.etree.ElementTree as ET


def xml_to_csv(xml_file, csv_file):
    """Convert XML data to CSV format"""

    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Film Title", "Rating"])

        for item in root.findall(".//item"):
            film_title = item.find(
                "letterboxd:filmTitle",
                namespaces={"letterboxd": "https://letterboxd.com"},
            )
            film_title = film_title.text if film_title is not None else ""

            member_rating = item.find(
                "letterboxd:memberRating",
                namespaces={"letterboxd": "https://letterboxd.com"},
            )
            member_rating = member_rating.text if member_rating is not None else ""
            csv_writer.writerow([film_title, member_rating])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xml_to_csv.py input.xml output.csv")
        sys.exit(1)

    xml_file = sys.argv[1]
    csv_file = sys.argv[2]

    xml_to_csv(xml_file, csv_file)
    print(f"Successfully converted {xml_file} to {csv_file}")
