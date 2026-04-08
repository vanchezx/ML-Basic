from abc import ABC, abstractmethod
from typing import List, Optional
from homework_04.media_base import MediaFile


class Storage(ABC):
    """Абстрактное хранилище файлов"""

    @abstractmethod
    def save(self, file: MediaFile, path: str) -> bool:
        """Сохранить файл в хранилище"""
        pass

    @abstractmethod
    def load(self, file_id: str) -> Optional[MediaFile]:
        """Загрузить файл из хранилища"""
        pass

    @abstractmethod
    def delete(self, file_id: str) -> bool:
        """Удалить файл из хранилища"""
        pass

    @abstractmethod
    def list_files(self) -> List[str]:
        """Список всех файлов в хранилище"""
        pass

    @abstractmethod
    def update(self, file_id: str, new_metadata: dict) -> bool:
        """Обновить метаданные файла"""
        pass


class LocalStorage(Storage):
    """Локальное файловое хранилище"""

    def __init__(self, base_path: str = "./media"):
        self.base_path = base_path
        self._files_cache: dict = {}

    def save(self, file: MediaFile, path: str) -> bool:
        """Сохранить файл локально"""
        # TODO: реальная запись на диск
        full_path = f"{self.base_path}/{path}/{file.name}"
        print(f"LocalStorage: Сохранение файла {file.name} по пути {full_path}")
        self._files_cache[file.name] = file
        return True

    def load(self, file_id: str) -> Optional[MediaFile]:
        """Загрузить файл из локального хранилища"""
        # TODO: реальное чтение с диска
        print(f"LocalStorage: Загрузка файла {file_id}")
        return self._files_cache.get(file_id)

    def delete(self, file_id: str) -> bool:
        """Удалить файл локально"""
        # TODO: реальное удаление с диска
        print(f"LocalStorage: Удаление файла {file_id}")
        if file_id in self._files_cache:
            del self._files_cache[file_id]
            return True
        return False

    def list_files(self) -> List[str]:
        """Список локальных файлов"""
        return list(self._files_cache.keys())

    def update(self, file_id: str, new_metadata: dict) -> bool:
        """Обновить метаданные локального файла"""
        if file_id in self._files_cache:
            self._files_cache[file_id].metadata.update(new_metadata)
            print(f"LocalStorage: Обновлены метаданные файла {file_id}")
            return True
        return False


class CloudStorage(Storage):
    """Облачное хранилище (S3-like)"""

    def __init__(self, bucket_name: str, access_key: str, secret_key: str):
        self.bucket_name = bucket_name
        self.access_key = access_key
        self.secret_key = secret_key

    def save(self, file: MediaFile, path: str) -> bool:
        """Сохранить файл в облако"""
        # TODO: реальная загрузка в S3
        print(f"CloudStorage: Загрузка {file.name} в бакет {self.bucket_name}/{path}")
        return True

    def load(self, file_id: str) -> Optional[MediaFile]:
        """Загрузить файл из облака"""
        # TODO: реальная загрузка из S3
        print(f"CloudStorage: Скачивание файла {file_id}")
        return None

    def delete(self, file_id: str) -> bool:
        """Удалить файл из облака"""
        print(f"CloudStorage: Удаление {file_id} из бакета {self.bucket_name}")
        return True

    def list_files(self) -> List[str]:
        """Список файлов в облаке"""
        # TODO: запрос к S3
        return []

    def update(self, file_id: str, new_metadata: dict) -> bool:
        """Обновить метаданные в облаке"""
        print(f"CloudStorage: Обновление метаданных {file_id}")
        return True


class RemoteStorage(Storage):
    """Удаленный сервер (FTP/SFTP/SSH)"""

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def save(self, file: MediaFile, path: str) -> bool:
        """Сохранить файл на удаленный сервер"""
        print(f"RemoteStorage: Загрузка {file.name} на {self.host}:{self.port}/{path}")
        return True

    def load(self, file_id: str) -> Optional[MediaFile]:
        """Загрузить файл с удаленного сервера"""
        print(f"RemoteStorage: Скачивание {file_id} с {self.host}")
        return None

    def delete(self, file_id: str) -> bool:
        """Удалить файл на удаленном сервере"""
        print(f"RemoteStorage: Удаление {file_id} на {self.host}")
        return True

    def list_files(self) -> List[str]:
        """Список файлов на удаленном сервере"""
        return []

    def update(self, file_id: str, new_metadata: dict) -> bool:
        """Обновить метаданные на удаленном сервере"""
        print(f"RemoteStorage: Обновление метаданных {file_id}")
        return True