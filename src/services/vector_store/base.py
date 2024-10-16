from abc import ABC, abstractmethod

from src.schemas.repository import (
    RepositoryDocument,
    RepositoryMetadata,
    RepositoryResponse,
)


class VectorStoreBase(ABC):
    @abstractmethod
    async def create_repository(self, name: str, metadata: RepositoryMetadata) -> str:
        pass

    @abstractmethod
    async def add_repository_documents(
        self, name: str, documents: list[RepositoryDocument], timestamp: str
    ) -> list[str]:
        pass

    @abstractmethod
    async def get_repository(self, name: str) -> RepositoryResponse:
        pass

    @abstractmethod
    async def get_repository_documents(
        self, name: str, limit: int | None, offset: int | None
    ) -> list[RepositoryDocument]:
        pass

    @abstractmethod
    async def get_all_repositories(self) -> list[RepositoryResponse]:
        pass

    @abstractmethod
    async def delete_repository(self, name: str) -> None:
        pass

    @abstractmethod
    async def delete_repository_documents(self, name: str, doc_ids: list[str]) -> None:
        pass

    @abstractmethod
    async def search_repository(
        self, name: str, query: str
    ) -> list[RepositoryDocument]:
        pass

    @abstractmethod
    async def update_repository_timestamp(self, name: str, timestamp: str) -> str:
        pass
