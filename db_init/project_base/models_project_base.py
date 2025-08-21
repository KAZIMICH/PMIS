# db_init/project_base/models_project_base.py

from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from db_init.base import Base


class ProjectBase(Base):
    __tablename__ = "project_base"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, comment="Название проекта")
    created_at = Column(DateTime, server_default=func.now(), nullable=False, comment="Дата создания")
    start_date = Column(DateTime, nullable=True, comment="Дата начала проекта")
    end_date = Column(DateTime, nullable=True, comment="Дата завершения проекта")
    status = Column(String(100), nullable=True, comment="Статус проекта")
    owner = Column(String(255), nullable=True, comment="Ответственный за проект")
    is_archive = Column(Boolean, default=False, nullable=False, comment="Проект архивный?")
    proj_type = Column(String(50), nullable=False, comment="Тип проекта")

    __mapper_args__ = {
        'polymorphic_identity': 'base',
        'polymorphic_on': proj_type
    }

    def __repr__(self):
        return f"<ProjectBase(id={self.id}, name={self.name}, type={self.proj_type})>"
