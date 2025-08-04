from vinyl.domain.models import Album
from vinyl.models import AlbumModel

class AlbumRepository:
    @staticmethod
    def save(album: Album) -> Album:
        if album.id:
            obj = AlbumModel.objects.get(pk=album.id)
            obj.title = album.title
            obj.artist = album.artist
            obj.year = album.year
            obj.genre = album.genre
        else:
            obj = AlbumModel(
                title=album.title,
                artist=album.artist,
                year=album.year,
                genre=album.genre,
            )
        obj.save()
        album.id = obj.id
        return album
