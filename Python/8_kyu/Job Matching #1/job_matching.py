from itertools import product


def job_matching(*, candidate: dict, job: dict) -> bool:
    candidate_offer = candidate.get('min_salary', None)
    company_offer = job.get('max_salary', None)

    if not candidate_offer or not company_offer:
        raise Exception('Error!')

    candidate_adjusted_offer = candidate_offer * 0.9

    if candidate_adjusted_offer <= company_offer:
        return True

    return False