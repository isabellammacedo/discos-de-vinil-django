from dataclasses import dataclass
from typing import Optional

@dataclass
class Album:
    id: Optional[int]
    title: str
    artist: str
    year: Optional[int] = None
    genre: Optional[str] = None

    def validate(self):
        if not self.title:
            raise ValueError("O título do álbum é obrigatório.")
        if self.year and (self.year < 1900 or self.year > 2100):
            raise ValueError("Ano inválido.")
        
