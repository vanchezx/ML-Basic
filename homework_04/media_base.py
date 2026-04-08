from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict, Any


class MediaFile(ABC):

    def __init__(
            self,
            name: str,
            size: int,
            owner: str,
            created_at: Optional[datetime] = None,
            **kwargs
    ):
        self.name = name
        self.size = size  # в байтах
        self.owner = owner
        self.created_at = created_at or datetime.now()
        self.metadata: Dict[str, Any] = kwargs

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """Вернуть все метаданные файла"""
        pass

    @abstractmethod
    def validate(self) -> bool:
        """Проверить валидность файла"""
        pass


class MediaActions(ABC):

    @abstractmethod
    def convert(self, target_format: str) -> 'MediaFile':
        """Конвертировать файл в другой формат"""
        pass

    @abstractmethod
    def extract_features(self) -> Dict[str, Any]:
        """Извлечь признаки или фичи из файла"""
        pass

    @abstractmethod
    def get_thumbnail(self, size: tuple = (100, 100)) -> bytes:
        """Получить миниатюру файла"""
        pass