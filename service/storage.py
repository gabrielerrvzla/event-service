from minio import Minio as MinioClient

from .settings import Settings


class Minio:
    def __init__(self, settings: Settings):
        self.client = MinioClient(
            settings.MINIO_HOST,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
            cert_check=settings.MINIO_CERT_CHECK,
        )

    def download(
        self,
        bucket: str,
        path_file: str,
        path_save: str,
    ) -> None:
        self.client.fget_object(bucket, path_file, path_save)

    def upload(
        self,
        bucket: str,
        file_path: str,
        save_path: str,
        content_type: str,
    ) -> None:
        self.client.fput_object(
            bucket_name=bucket,
            object_name=save_path,
            file_path=file_path,
            content_type=content_type,
        )
