import json

__data = []


def load_candidates_form_json(path):
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = []
    for candidate in __data:
        if candidate_name.lower() in candidate['name'].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __data:
        if skill_name in candidate['skills']:
            candidates.append(candidate)
    return candidates

