# coding: utf8
# Standard library imports...
from mock import patch

# Third-party imports...
from nose.tools import assert_list_equal

# Local imports...
from project.services import get_todos

# 这个测试适用于后续的更新迭代，因为数据交互的结构有可能会变动，所以最好比较实际API与mock的结构。
def test_integration_contract():
    # Call the service to hit the actual API.
    actual = get_todos()
    actual_keys = actual.json().pop().keys()

    # Call the service to hit the mocked API.
    with patch('project.services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()

    # An object from the actual API and an object from the mocked API should have
    # the same data structure.
    assert_list_equal(list(actual_keys), list(mocked_keys))
