from typing import List, Dict, Any
from homework_04.media_base import MediaFile
from homework_04.storage import Storage


class MediaManager:
    """Менеджер для работы с медиа-файлами"""

    def __init__(self, storage: Storage):
        self.storage = storage

    def upload_file(self, file: MediaFile, path: str) -> bool:
        """Загрузить файл в хранилище"""
        if not file.validate():
            raise ValueError(f"Файл {file.name} не прошел валидацию")
        return self.storage.save(file, path)

    def download_file(self, file_id: str) -> MediaFile:
        """Скачать файл из хранилища"""
        file = self.storage.load(file_id)
        if file is None:
            raise FileNotFoundError(f"Файл {file_id} не найден")
        return file

    def delete_file(self, file_id: str) -> bool:
        """Удалить файл"""
        return self.storage.delete(file_id)

    def convert_file(self, file: MediaFile, target_format: str) -> MediaFile:
        """Конвертировать файл"""
        return file.convert(target_format)

    def batch_extract_features(self, files: List[MediaFile]) -> List[Dict[str, Any]]:
        """Массовое извлечение признаков"""
        return [f.extract_features() for f in files]