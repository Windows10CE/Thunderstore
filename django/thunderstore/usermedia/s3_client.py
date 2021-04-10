import boto3
from django.conf import settings
from mypy_boto3_s3 import Client

from thunderstore.usermedia.exceptions import S3ConfigurationException


def get_s3_client(for_signing: bool = False) -> "Client":
    if not all(
        (
            settings.AWS_S3_ENDPOINT_URL,
            settings.AWS_ACCESS_KEY_ID,
            settings.AWS_SECRET_ACCESS_KEY,
        )
    ):
        raise S3ConfigurationException

    endpoint = settings.AWS_S3_ENDPOINT_URL
    if for_signing and settings.AWS_S3_SIGNING_ENDPOINT_URL:
        endpoint = settings.AWS_S3_SIGNING_ENDPOINT_URL

    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )
