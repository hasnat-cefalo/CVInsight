from abc import ABC, abstractmethod
from typing import List

from app.models.cv_model import CVModel


class BaseService(ABC):
    @abstractmethod
    def parse_cv(self, text: List[str]) -> CVModel:
        """Parse CV text using the specific service."""
        pass
