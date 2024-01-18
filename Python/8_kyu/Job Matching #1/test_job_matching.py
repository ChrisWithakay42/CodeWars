from itertools import product

import pytest
from job_matching import job_matching

test_data = [
    ({'min_salary': 120000}, {'max_salary': 130000}, True),
    ({'min_salary': 120000}, {'max_salary': 80000}, False),
    ({'min_salary': 120000}, {'max_salary': 171000}, True),
    ({'min_salary': 190000}, {'max_salary': 130000}, False),
    ({'min_salary': 190000}, {'max_salary': 80000}, False),
    ({'min_salary': 190000}, {'max_salary': 171000}, True),
]


@pytest.mark.parametrize('candidate, job, result', test_data)
def test_job_matching(candidate, job, result):
    assert job_matching(candidate=candidate, job=job) == result


def test_raise_exception():
    with pytest.raises(Exception):
        assert job_matching(candidate={}, job={'max_salary': 190000})
        assert job_matching(candidate={'min_salary': 190000}, job={})
