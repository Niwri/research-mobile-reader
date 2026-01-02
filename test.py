import json
import bibtexparser

def bibtex_to_json(bib_path, json_path):
    with open(bib_path, 'r', encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    bibliographies = {}
    for entry in bib_database.entries:
        key = entry.pop('ID')
        bibliographies[key] = entry

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump({"bibliographies": bibliographies}, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    bibtex_to_json(
        r"unit-tests/data/test_1/arXiv-2502.00211v1/paper.bib",
        r"unit-tests/data/test_1/bib.json"
    )