# db_init/project_base/crud_project_base.py

from sqlalchemy.orm import Session
from db_init.project_base.models_project_base import ProjectBase
from typing import Optional

class ProjectBaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_base_project(self, name: str, start_date=None, end_date=None, status: Optional[str] = None,
                             owner: Optional[str] = None, is_archive: bool = False) -> ProjectBase:
        project = ProjectBase(
            name=name,
            start_date=start_date,
            end_date=end_date,
            status=status,
            owner=owner,
            is_archive=is_archive,
            proj_type="base"
        )
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update_base_project(self, **kwargs) -> Optional[ProjectBase]:
        project = self.get_base_project()
        if not project:
            return None
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_base_project(self) -> Optional[ProjectBase]:
        """
        Получает базовый проект по его типу.
        """
        return (
            self.db.query(ProjectBase)
            .filter(ProjectBase.proj_type == "base")
            .first()
        )
