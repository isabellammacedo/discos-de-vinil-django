from vinyl.domain.models import Album
from vinyl.infrastructure.repositories import AlbumRepository

class AlbumService:
    @staticmethod
    def create_album(data: dict) -> Album:
        album = Album(
            id=None,
            title=data.get('title'),
            artist=data.get('artist'),
            year=data.get('year'),
            genre=data.get('genre'),
        )
        album.validate()
        return AlbumRepository.save(album)
