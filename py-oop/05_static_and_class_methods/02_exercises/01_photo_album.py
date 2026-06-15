class PhotoAlbum:
    _max_photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self. photos =[[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        resulting_pages = (photos_count // cls._max_photos_per_page)
        if photos_count % cls._max_photos_per_page == 0:

            return cls(resulting_pages)

        return cls(resulting_pages + 1)

    def get_count_photos(self):
        count_photos = sum(1 for page in self.photos for _ in page)

        return count_photos


    def add_photo(self, label: str):
        photos = self.get_count_photos()
        if photos == self._max_photos_per_page * self.pages:

            return "No more free slots"

        page = photos // self._max_photos_per_page
        self.photos[page].append(label)

        slot = len(self.photos[page])

        return f"{label} photo added successfully on page {page + 1} slot {slot}"

    @staticmethod
    def get_page_separation():
        return f"{'-' * 11}\n"

    def display(self):
        result = ''
        for page in self.photos:
                result += self.get_page_separation()
                result += " ".join('[]' for photo in page) + '\n'

        return result + self.get_page_separation()


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())


album = PhotoAlbum.from_photos_count(12)
print(album.pages) # 3
print(album.display())