from typing import Dict, Any, Callable, Iterable, Optional

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[Dict[str, Any]], Dict[str, Any]]

def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    for row in data:
        row = selector(row)
        if all(filter_func(row) is not None for filter_func in filters):
            yield row


def select(*rows: str) -> ModifierFunc:
    def inner(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in data.items() if k in rows}
    return inner


def field_filter(column: str, *values: Any) -> ModifierFunc:
    def inner(row: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if row[column] in values:
            return row
        else:
            return None
    return inner


def test_query():
    friends = [
        {"name": "Sam", "gender": "male", "sport": "Basketball"},
        {"name": "Emily", "gender": "female", "sport": "Volleyball"}
    ]
    value = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Basketball', 'Volleyball'),
        field_filter('gender', 'male',),
    )
    result = list(value)
    print(result)
    assert result == [
        {"name": "Sam", "gender": "male", "sport": "Basketball"}
    ]

if __name__ == "__main__":
    test_query()