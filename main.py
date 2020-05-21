import scraper
from relation_table import RelationTable
from visit_table import VisitTable
import requests


def process_path(start_url: str, target: str, relation_table: RelationTable, visit_table: VisitTable, path: list):
    new_path = path.copy()
    new_path.append(start_url)
    if start_url == target:
        return new_path
    if len(new_path) >= 5:
        return None
    links = scraper.get_links(start_url)
    if len(links) == 0:
        return None
    print("\t" * (len(new_path) - 1) + start_url)
    for link in links:
        relation_table.add_relation(start_url, link)
    visit_table.visit(start_url)
    neighbors = relation_table.get_unvisited_neighbors(start_url, visit_table)
    for neighbor in neighbors:
        if neighbor == target:
            new_path.append(neighbor)
            return new_path
    if len(neighbors) == 0:
        return None
    if len(new_path) == 4:
        return None
    for neighbor in neighbors:
        next_path = process_path(neighbor, target, relation, visit_table, new_path)
        if next_path is not None:
            return next_path


def get_url(prompt):
    url = input(prompt)
    page = requests.get("https://en.wikipedia.org/wiki/" + url)
    if page.status_code == 200:
        return url
    print("That wiki page does not exist!")
    return get_url(prompt)


if __name__ == '__main__':
    start_url = get_url("Enter starting point! ")
    target_url = get_url("Enter Target point! ")
    relation = RelationTable()
    visit = VisitTable()
    p = []
    p = process_path(start_url, target_url, relation, visit, p)
    print(" -> ".join(p))
