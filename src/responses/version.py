from src.responses.base import ResponseBase


class VersionResponse(ResponseBase):
    """
    バージョン取得用エンドポイントのレスポンスクラス

    Attributes:
        - version (str): バージョン
    """

    version: str
