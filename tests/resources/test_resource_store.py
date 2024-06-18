import pytest

from src.resources.resource_store import ResourceStore


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("HelloWorldFunction.Properties.Handler", True),
        ("simple.path", True),
        ("Invalid-Path", False),
        ("another.valid.path_123", True),
        ("123invalid.start", False),
    ],
)
def test_is_valid_dot_notation(test_input, expected):
    assert ResourceStore.is_valid_dot_notation(test_input) == expected


@pytest.mark.parametrize(
    "path,resources,expected",
    [
        ("Test.TestArn", {"Test": {"TestArn": "test"}}, "test"),
        (
            "Test.Nested1.Nested2.Nested3",
            {"Test": {"Nested1": {"Nested2": {"Nested3": "deeply-nested"}}}},
            "deeply-nested",
        ),
    ],
)
def test_get_attribute(path, resources, expected):
    resource_store = ResourceStore(resources)
    assert resource_store.get_attribute(path) == expected
