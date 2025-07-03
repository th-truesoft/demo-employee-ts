from typing import List, Optional, Dict, Any, Union
from sqlalchemy.orm import Session

from app.models.employee import Employee, Department, Position, Location
from app.repositories.employee import (
    employee_repository, department_repository, position_repository, location_repository
)
from app.schemas.employee import (
    EmployeeCreate, EmployeeUpdate, EmployeeSearchFilters,
    DepartmentCreate, DepartmentUpdate,
    PositionCreate, PositionUpdate,
    LocationCreate, LocationUpdate
)


class EmployeeService:
    def get(self, db: Session, employee_id: int) -> Optional[Employee]:
        return employee_repository.get(db=db, id=employee_id)

    def search(
        self, db: Session, *, filters: EmployeeSearchFilters
    ) -> List[Employee]:
        return employee_repository.search(db=db, filters=filters)
    
    def count(
        self, db: Session, *, filters: EmployeeSearchFilters
    ) -> int:
        return employee_repository.count(db=db, filters=filters)
    
    def create(self, db: Session, *, obj_in: EmployeeCreate) -> Employee:
        return employee_repository.create(db=db, obj_in=obj_in)

    def update(
        self, db: Session, *, db_obj: Employee, obj_in: Union[EmployeeUpdate, Dict[str, Any]]
    ) -> Employee:
        return employee_repository.update(db=db, db_obj=db_obj, obj_in=obj_in)

    def delete(self, db: Session, *, employee_id: int) -> Employee:
        return employee_repository.remove(db=db, id=employee_id)


class DepartmentService:
    def get(self, db: Session, department_id: int) -> Optional[Department]:
        return department_repository.get(db=db, id=department_id)

    def get_by_name(self, db: Session, *, name: str) -> Optional[Department]:
        return department_repository.get_by_name(db=db, name=name)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Department]:
        return department_repository.get_multi(db=db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: DepartmentCreate) -> Department:
        return department_repository.create(db=db, obj_in=obj_in)

    def update(
        self, db: Session, *, db_obj: Department, obj_in: Union[DepartmentUpdate, Dict[str, Any]]
    ) -> Department:
        return department_repository.update(db=db, db_obj=db_obj, obj_in=obj_in)

    def delete(self, db: Session, *, department_id: int) -> Department:
        return department_repository.remove(db=db, id=department_id)


class PositionService:
    def get(self, db: Session, position_id: int) -> Optional[Position]:
        return position_repository.get(db=db, id=position_id)

    def get_by_name(self, db: Session, *, name: str) -> Optional[Position]:
        return position_repository.get_by_name(db=db, name=name)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Position]:
        return position_repository.get_multi(db=db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: PositionCreate) -> Position:
        return position_repository.create(db=db, obj_in=obj_in)

    def update(
        self, db: Session, *, db_obj: Position, obj_in: Union[PositionUpdate, Dict[str, Any]]
    ) -> Position:
        return position_repository.update(db=db, db_obj=db_obj, obj_in=obj_in)

    def delete(self, db: Session, *, position_id: int) -> Position:
        return position_repository.remove(db=db, id=position_id)


class LocationService:
    def get(self, db: Session, location_id: int) -> Optional[Location]:
        return location_repository.get(db=db, id=location_id)

    def get_by_name(self, db: Session, *, name: str) -> Optional[Location]:
        return location_repository.get_by_name(db=db, name=name)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Location]:
        return location_repository.get_multi(db=db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: LocationCreate) -> Location:
        return location_repository.create(db=db, obj_in=obj_in)

    def update(
        self, db: Session, *, db_obj: Location, obj_in: Union[LocationUpdate, Dict[str, Any]]
    ) -> Location:
        return location_repository.update(db=db, db_obj=db_obj, obj_in=obj_in)

    def delete(self, db: Session, *, location_id: int) -> Location:
        return location_repository.remove(db=db, id=location_id)


employee_service = EmployeeService()
department_service = DepartmentService()
position_service = PositionService()
location_service = LocationService()
