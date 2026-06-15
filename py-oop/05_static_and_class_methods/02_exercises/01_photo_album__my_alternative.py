# My solution using initialization with None, judge seems to expect empty lists
class PhotoAlbum:
    _max_photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self. photos = [[None for _ in range(self._max_photos_per_page)] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        resulting_pages = (photos_count // cls._max_photos_per_page) + 1

        return cls(resulting_pages)


    def get_free_pos(self):
        for i in range(self.pages):
            for j in range(self._max_photos_per_page):
                if not self.photos[i][j]:

                    return i, j

    def add_photo(self, label: str):
        if any(False for page in self.photos for pic in page if pic is None):

            return f"No more free slots"

        page, picture = self.get_free_pos()
        self.photos[page][picture] = label

        return f"{label} photo added successfully on page {page + 1} slot {picture + 1}"

    @staticmethod
    def get_page_separation():
        return f"{'-' * 11}\n"
    #TODO wrap the joined photos with the dashes
    def display(self):
        result = ''
        for page in self.photos:
                result += self.get_page_separation()
                result += " ".join('[]' for photo in page if photo) + '\n'

        return result + self.get_page_separation()

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
