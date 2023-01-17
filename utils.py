import json


def load_candidates_from_json(path):
    candidates_data = []
    with open(path, 'r', encoding="utf-8") as file:
        candidates_data = json.load(file)
    return candidates_data


def get_candidate(candidate_id):
    candidates_data=load_candidates_from_json(r"D:\Py_projects\flask_begin\candidates.json")
    for candidate in candidates_data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'ничего не найдено'}


def get_candidates_by_name(candidate_name):
    candidates_data = load_candidates_from_json(r"D:\Py_projects\flask_begin\candidates.json")
    return [candidate for candidate in candidates_data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates_data = load_candidates_from_json(r"D:\Py_projects\flask_begin\candidates.json")
    candidates = []
    for candidate in candidates_data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
