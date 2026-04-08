from typing import Dict, Any, Optional
from homework_04.media_base import MediaFile, MediaActions


class AudioFile(MediaFile, MediaActions):
    """Аудио файл"""

    def __init__(
            self,
            name: str,
            size: int,
            owner: str,
            duration: float,
            bitrate: int,
            sample_rate: int,
            **kwargs
    ):
        super().__init__(name, size, owner, **kwargs)
        self.duration = duration
        self.bitrate = bitrate
        self.sample_rate = sample_rate

    def get_metadata(self) -> Dict[str, Any]:
        return {
            'type': 'audio',
            'name': self.name,
            'size': self.size,
            'owner': self.owner,
            'created_at': self.created_at,
            'duration': self.duration,
            'bitrate': self.bitrate,
            'sample_rate': self.sample_rate,
            **self.metadata
        }

    def validate(self) -> bool:
        return self.size > 0 and self.duration > 0 and 32 <= self.bitrate <= 320

    def convert(self, target_format: str) -> 'AudioFile':
        """Конвертация в другой формат"""
        pass

    def extract_features(self) -> Dict[str, Any]:
        """Извлечение фич"""
        pass

    def get_thumbnail(self, size: tuple = (100, 100)) -> bytes:
        """Получить обложку альбома или визуализацию аудио"""
        pass


class VideoFile(MediaFile, MediaActions):
    """Видео файл"""

    def __init__(
            self,
            name: str,
            size: int,
            owner: str,
            duration: float,
            width: int,
            height: int,
            fps: float,
            codec: str,
            **kwargs
    ):
        super().__init__(name, size, owner, **kwargs)
        self.duration = duration
        self.width = width
        self.height = height
        self.fps = fps
        self.codec = codec

    def get_metadata(self) -> Dict[str, Any]:
        return {
            'type': 'video',
            'name': self.name,
            'size': self.size,
            'owner': self.owner,
            'created_at': self.created_at,
            'duration': self.duration,
            'resolution': f"{self.width}x{self.height}",
            'fps': self.fps,
            'codec': self.codec,
            **self.metadata
        }

    def validate(self) -> bool:
        return self.size > 0 and self.duration > 0 and self.width > 0 and self.height > 0 and self.fps > 0

    def convert(self, target_format: str) -> 'VideoFile':
        """Конвертация в другой формат"""
        pass

    def extract_features(self) -> Dict[str, Any]:
        """Извлечение фич"""
        pass

    def get_thumbnail(self, size: tuple = (100, 100)) -> bytes:
        """Получить кадр из видео"""
        pass


class PhotoFile(MediaFile, MediaActions):
    """Фото файл"""

    def __init__(
            self,
            name: str,
            size: int,
            owner: str,
            width: int,
            height: int,
            color_depth: int,
            camera_model: Optional[str] = None,
            **kwargs
    ):
        super().__init__(name, size, owner, **kwargs)
        self.width = width
        self.height = height
        self.color_depth = color_depth
        self.camera_model = camera_model

    def get_metadata(self) -> Dict[str, Any]:
        return {
            'type': 'photo',
            'name': self.name,
            'size': self.size,
            'owner': self.owner,
            'created_at': self.created_at,
            'resolution': f"{self.width}x{self.height}",
            'color_depth': self.color_depth,
            'camera_model': self.camera_model,
            **self.metadata
        }

    def validate(self) -> bool:
        return self.size > 0 and self.width > 0 and self.height > 0

    def convert(self, target_format: str) -> 'PhotoFile':
        """Конвертация в другой формат"""
        pass

    def extract_features(self) -> Dict[str, Any]:
        """Извлечение фич"""
        pass

    def get_thumbnail(self, size: tuple = (100, 100)) -> bytes:
        """Создать уменьшенную копию фото"""
        pass