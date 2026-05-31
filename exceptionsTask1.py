import textwrap

class Pagination:

    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.wrapped_list = textwrap.wrap(
            self.data, self.items_on_page, drop_whitespace=False,
        )

    def __getattr__(self, attr):
        if attr == "item_count":
            return len(self.data)
        if attr == "page_count":
            #print(self.wrapped_list)
            return len(self.wrapped_list)
        raise TypeError("Wrong attr")

    def count_items_on_page(self, page_number):
        try:
            return len(self.wrapped_list[page_number])
        except Exception:
            raise IndexError("Invalid index. Page is missing.")

    def find_page(self, data):
        querying_pages = []
        for elem in self.wrapped_list:
            if elem.strip() in data or data in elem:
                querying_pages.append(self.wrapped_list.index(elem))
        if querying_pages:
            return querying_pages
        raise ValueError(f"{data} is missing on the pages")

    def display_page(self, page_number):
        try:
            return self.wrapped_list[page_number]
        except Exception:
            raise IndexError("Invalid index. Page is missing.")


pages = Pagination('Your beautiful text', 5)
if __name__ == "__main__":
    assert pages.page_count == 4
    assert pages.item_count == 19
    assert pages.count_items_on_page(3) == 4
    assert pages.find_page('text') == [3]
    assert pages.display_page(0) == 'Your '