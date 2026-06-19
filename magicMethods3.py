from abc import ABC, abstractmethod
import functools
from typing import Any

class Currency(ABC):
    rate_to_euro: float = 1.0
    currency_code: str = ""

    def __init__(self, nominal_volume: Any):
        # Force nominal_volume to a float so it consistently prints with '.0'
        self.nominal_volume = float(nominal_volume)

    @classmethod
    @abstractmethod
    def course(cls, other_currency: type["Currency"]) -> str:
        pass

    @abstractmethod
    def to_currency(self, currency: type["Currency"]) -> "Currency":
        pass


@functools.total_ordering
class Euro(Currency):
    rate_to_euro = 1.0
    currency_code = "EUR"

    @classmethod
    def course(cls, other_currency: type[Currency]) -> str:
        current_course = other_currency.rate_to_euro / cls.rate_to_euro
        return f"{current_course} {other_currency.currency_code} for 1 {cls.currency_code}"

    def to_currency(self, currency: type[Currency]) -> Currency:
        converted_volume = self.nominal_volume * currency.rate_to_euro / self.rate_to_euro
        return currency(converted_volume)

    def __repr__(self):
        return f"{self.nominal_volume} {self.currency_code}"

    def __gt__(self, other: Currency) -> bool:
        return self.nominal_volume > (other.nominal_volume / other.rate_to_euro)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Currency):
            return False
        return self.nominal_volume == (other.nominal_volume / other.rate_to_euro)

    def __add__(self, other: Currency) -> str:
        return f"{self.nominal_volume + (other.nominal_volume / other.rate_to_euro)} {self.currency_code}"


@functools.total_ordering
class Dollar(Currency):
    rate_to_euro = 2.0
    currency_code = "USD"

    @classmethod
    def course(cls, other_currency: type[Currency]) -> str:
        current_course = other_currency.rate_to_euro / cls.rate_to_euro
        return f"{current_course} {other_currency.currency_code} for 1 {cls.currency_code}"

    def to_currency(self, currency: type[Currency]) -> Currency:
        converted_volume = self.nominal_volume * currency.rate_to_euro / self.rate_to_euro
        return currency(converted_volume)

    def __repr__(self):
        return f"{self.nominal_volume} {self.currency_code}"

    def __gt__(self, other: Currency) -> bool:
        return (self.nominal_volume / self.rate_to_euro) > (other.nominal_volume / other.rate_to_euro)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Currency):
            return False
        return (self.nominal_volume / self.rate_to_euro) == (other.nominal_volume / other.rate_to_euro)

    def __add__(self, other: Currency) -> str:
        val = ((self.nominal_volume / self.rate_to_euro) + (other.nominal_volume / other.rate_to_euro)) * self.rate_to_euro
        return f"{val} {self.currency_code}"


@functools.total_ordering
class Pound(Currency):
    rate_to_euro = 100.0
    currency_code = "GBP"

    @classmethod
    def course(cls, other_currency: type[Currency]) -> str:
        current_course = other_currency.rate_to_euro / cls.rate_to_euro
        return f"{current_course} {other_currency.currency_code} for 1 {cls.currency_code}"

    def to_currency(self, currency: type[Currency]) -> Currency:
        converted_volume = self.nominal_volume * currency.rate_to_euro / self.rate_to_euro
        return currency(converted_volume)

    def __repr__(self):
        return f"{self.nominal_volume} {self.currency_code}"

    def __gt__(self, other: Currency) -> bool:
        return (self.nominal_volume / self.rate_to_euro) > (other.nominal_volume / other.rate_to_euro)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Currency):
            return False
        return (self.nominal_volume / self.rate_to_euro) == (other.nominal_volume / other.rate_to_euro)

    def __add__(self, other: Currency) -> str:
        val = ((self.nominal_volume / self.rate_to_euro) + (other.nominal_volume / other.rate_to_euro)) * self.rate_to_euro
        return f"{val} {self.currency_code}"


def su(data):
    cash = 0.0
    currency_code = ""
    for i in data:
        string = str(i).split()
        cash += float(string[0])
        currency_code = string[1]
    return f"{cash} {currency_code}"


if __name__ == "__main__":
    # --- Class-Level Course Calculations (Pytest Suite 1) ---
    assert Euro.course(Dollar) == "2.0 USD for 1 EUR"
    assert Euro.course(Pound) == "100.0 GBP for 1 EUR"
    assert Euro.course(Euro) == "1.0 EUR for 1 EUR"

    assert Dollar.course(Euro) == "0.5 EUR for 1 USD"
    assert Dollar.course(Pound) == "50.0 GBP for 1 USD"
    assert Dollar.course(Dollar) == "1.0 USD for 1 USD"

    assert Pound.course(Dollar) == "0.02 USD for 1 GBP"
    assert Pound.course(Euro) == "0.01 EUR for 1 GBP"
    assert Pound.course(Pound) == "1.0 GBP for 1 GBP"

    # Instantiate objects for instance checks
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    # --- Instance-Level Conversion Asserts (Pytest Suite 2) ---
    # Note: Wrap object-returning transformations inside str() or f"{}" to check text format!
    assert f"{e}" == "100.0 EUR"
    assert f"{e.to_currency(Dollar)}" == "200.0 USD"
    assert f"{e.to_currency(Pound)}" == "10000.0 GBP"
    assert f"{e.to_currency(Euro)}" == "100.0 EUR"

    assert str(r) == "100.0 GBP"
    assert f"{r.to_currency(Dollar)}" == "2.0 USD"
    assert f"{r.to_currency(Euro)}" == "1.0 EUR"
    assert f"{r.to_currency(Pound)}" == "100.0 GBP"

    assert str(d) == "200.0 USD"
    assert f"{d.to_currency(Dollar)}" == "200.0 USD"
    assert f"{d.to_currency(Euro)}" == "100.0 EUR"
    assert f"{d.to_currency(Pound)}" == "10000.0 GBP"

    # --- Array Aggregation Checks ---
    assert su([Euro(100), Euro(50)]) == "150.0 EUR"

    print("All local and automated grading assertions passed successfully!")



    ### GIT PUSHED VERSION ###

# from abc import ABC
# import functools
# from typing import Any
#
#
# class Currency(ABC):
#     rate_to_euro: float = 1.0
#     currency_code: str = ""
#
#     def __init__(self, nominal_volume: float):
#         self.nominal_volume = float(nominal_volume)
#
#     @classmethod
#     def course(cls, other_currency: type["Currency"]) -> str:
#         """Computes the conversion rate between two class blueprints."""
#         current_course = other_currency.rate_to_euro / cls.rate_to_euro
#         return f"{current_course} {other_currency.currency_code} for 1 {cls.currency_code}"
#
#     def to_currency(self, currency: type["Currency"]) -> "Currency":
#         """Returns a brand-new instance of the target Currency class."""
#         converted_volume = self.nominal_volume * currency.rate_to_euro / self.rate_to_euro
#         return currency(converted_volume)
#
#     def __repr__(self) -> str:
#         return f"{self.nominal_volume} {self.currency_code}"
#
#     def __gt__(self, other: "Currency") -> bool:
#         return (self.nominal_volume / self.rate_to_euro) > (other.nominal_volume / other.rate_to_euro)
#
#     def __eq__(self, other: Any) -> bool:
#         if not isinstance(other, Currency):
#             return False
#         return (self.nominal_volume / self.rate_to_euro) == (other.nominal_volume / other.rate_to_euro)
#
#     def __add__(self, other: "Currency") -> "Currency":
#         """Adds two currencies and returns a new object matching the left-hand class."""
#         base_euros = (self.nominal_volume / self.rate_to_euro) + (other.nominal_volume / other.rate_to_euro)
#         converted_volume = base_euros * self.rate_to_euro
#         return self.__class__(converted_volume)
#
#
# @functools.total_ordering
# class Euro(Currency):
#     rate_to_euro = 1.0
#     currency_code = "EUR"
#
#
# @functools.total_ordering
# class Dollar(Currency):
#     rate_to_euro = 2.0
#     currency_code = "USD"
#
#
# @functools.total_ordering
# class Pound(Currency):
#     rate_to_euro = 100.0
#     currency_code = "GBP"
#
#
# def su(data: list[Currency]) -> str:
#     """Aggregates an arbitrary list of currencies using class-level reduction."""
#     if not data:
#         return "0.0 EUR"
#     total_currency = functools.reduce(lambda x, y: x + y, data)
#     return f"{float(total_currency.nominal_volume)} {total_currency.currency_code}"
#
#
# if __name__ == "__main__":
#     # --- Class-Level Course Calculations (Pytest Suite 1) ---
#     assert Euro.course(Dollar) == "2.0 USD for 1 EUR"
#     assert Euro.course(Pound) == "100.0 GBP for 1 EUR"
#     assert Euro.course(Euro) == "1.0 EUR for 1 EUR"
#
#     assert Dollar.course(Euro) == "0.5 EUR for 1 USD"
#     assert Dollar.course(Pound) == "50.0 GBP for 1 USD"
#     assert Dollar.course(Dollar) == "1.0 USD for 1 USD"
#
#     assert Pound.course(Dollar) == "0.02 USD for 1 GBP"
#     assert Pound.course(Euro) == "0.01 EUR for 1 GBP"
#     assert Pound.course(Pound) == "1.0 GBP for 1 GBP"
#
#     # Instantiate objects for instance checks
#     e = Euro(100)
#     r = Pound(100)
#     d = Dollar(200)
#
#     # --- Instance-Level Conversion Asserts (Pytest Suite 2) ---
#     assert str(e) == "100.0 EUR"
#     assert str(e.to_currency(Dollar)) == "200.0 USD"
#     assert str(e.to_currency(Pound)) == "10000.0 GBP"
#     assert str(e.to_currency(Euro)) == "100.0 EUR"
#
#     assert str(r) == "100.0 GBP"
#     assert str(r.to_currency(Dollar)) == "2.0 USD"
#     assert str(r.to_currency(Euro)) == "1.0 EUR"
#     assert str(r.to_currency(Pound)) == "100.0 GBP"
#
#     assert str(d) == "200.0 USD"
#     assert str(d.to_currency(Dollar)) == "200.0 USD"
#     assert str(d.to_currency(Euro)) == "100.0 EUR"
#     assert str(d.to_currency(Pound)) == "10000.0 GBP"
#
#     # --- Array Aggregation Checks ---
#     assert su([Euro(100), Euro(50)]) == "150.0 EUR"
#
#     print("All local and automated grading assertions passed successfully!")