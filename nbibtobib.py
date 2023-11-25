import re
import sys
import os

def nbib_to_bibtex(nbib_content):
    """
    Convert NBIB formatted content to a BibTeX entry.
    
    Args:
    nbib_content (str): The content of the NBIB file.

    Returns:
    str: The converted BibTeX entry.
    """
    # Define a dictionary to hold BibTeX fields
    bibtex_entry = {
        "type": "article",
        "citation_key": "",
        "title": "",
        "author": "",
        "journal": "",
        "year": "",
        "volume": "",
        "number": "",
        "pages": "",
        "doi": ""
    }

    # Regular expressions for different fields
    patterns = {
        "PMID": re.compile(r"PMID- (\d+)"),
        "title": re.compile(r"TI  - (.+)"),
        "authors": re.compile(r"AU  - (.+)"),
        "journal": re.compile(r"JT  - (.+)"),
        "year": re.compile(r"DP  - (\d{4})"),
        "volume": re.compile(r"VI  - (\w+)"),
        "issue": re.compile(r"IP  - (\w+)"),
        "pages": re.compile(r"PG  - (\w+-\w+)"),
        "doi": re.compile(r"LID - ([\w\.\/\:-]+) \[doi\]")
    }

    # Extracting fields
    for key, pattern in patterns.items():
        match = pattern.search(nbib_content)
        if match:
            bibtex_entry[key] = match.group(1)

    # Format the BibTeX entry
    bibtex_format = f"@{bibtex_entry['type']}{{{bibtex_entry['PMID']},\n"
    bibtex_format += f"  title = {{{bibtex_entry['title']}}},\n"
    bibtex_format += f"  author = {{{bibtex_entry['authors']}}},\n"
    bibtex_format += f"  journal = {{{bibtex_entry['journal']}}},\n"
    bibtex_format += f"  year = {{{bibtex_entry['year']}}},\n"
    bibtex_format += f"  volume = {{{bibtex_entry['volume']}}},\n"
    bibtex_format += f"  number = {{{bibtex_entry['issue']}}},\n"
    bibtex_format += f"  pages = {{{bibtex_entry['pages']}}},\n"
    bibtex_format += f"  doi = {{{bibtex_entry['doi']}}}\n"
    bibtex_format += "}"

    return bibtex_format

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file.nbib>")
        sys.exit(1)

    nbib_file = sys.argv[1]

    if not os.path.exists(nbib_file):
        print(f"File {nbib_file} not found.")
        sys.exit(1)

    with open(nbib_file, 'r') as file:
        nbib_content = file.read()

    bibtex_content = nbib_to_bibtex(nbib_content)

    output_file = nbib_file.replace('.nbib', '.bib')
    with open(output_file, 'w') as file:
        file.write(bibtex_content)

    print(f"BibTeX file created: {output_file}")

if __name__ == "__main__":
    main()
