import reflex as rx
from typing import TypedDict
import asyncio


class Employee(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    role: str
    department: str
    hire_date: str
    salary: str
    is_active: bool


class EmployeeState(rx.State):
    employees: list[Employee] = []
    search_query: str = ""
    filter_department: str = "All"
    view_mode: str = "grid"
    show_detail_modal: bool = False
    show_add_edit_modal: bool = False
    is_editing: bool = False
    selected_employee: Employee | None = None
    new_employee_data: Employee = {
        "id": 0,
        "name": "",
        "email": "",
        "phone": "",
        "role": "",
        "department": "Engineering",
        "hire_date": "",
        "salary": "",
        "is_active": True,
    }

    @rx.event
    async def load_employees(self):
        await asyncio.sleep(0.5)
        self.employees = [
            {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice.j@example.com",
                "phone": "123-456-7890",
                "role": "Software Engineer",
                "department": "Engineering",
                "hire_date": "2022-01-15",
                "salary": "$90,000",
                "is_active": True,
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "email": "bob.s@example.com",
                "phone": "234-567-8901",
                "role": "Product Manager",
                "department": "Product",
                "hire_date": "2021-11-20",
                "salary": "$110,000",
                "is_active": True,
            },
            {
                "id": 3,
                "name": "Charlie Brown",
                "email": "charlie.b@example.com",
                "phone": "345-678-9012",
                "role": "UX Designer",
                "department": "Design",
                "hire_date": "2022-03-10",
                "salary": "$85,000",
                "is_active": True,
            },
            {
                "id": 4,
                "name": "Diana Prince",
                "email": "diana.p@example.com",
                "phone": "456-789-0123",
                "role": "Data Scientist",
                "department": "Engineering",
                "hire_date": "2023-05-25",
                "salary": "$100,000",
                "is_active": False,
            },
            {
                "id": 5,
                "name": "Ethan Hunt",
                "email": "ethan.h@example.com",
                "phone": "567-890-1234",
                "role": "Marketing Lead",
                "department": "Marketing",
                "hire_date": "2020-08-01",
                "salary": "$95,000",
                "is_active": True,
            },
        ]

    @rx.var
    def filtered_employees(self) -> list[Employee]:
        employees = self.employees
        if self.filter_department != "All":
            employees = [
                e for e in employees if e["department"] == self.filter_department
            ]
        if self.search_query:
            search_lower = self.search_query.lower()
            employees = [
                e
                for e in employees
                if search_lower in e["name"].lower()
                or search_lower in e["role"].lower()
            ]
        return employees

    @rx.var
    def department_options(self) -> list[str]:
        departments = {"All"} | {e["department"] for e in self.employees}
        return sorted(list(departments))

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_filter_department(self, department: str):
        self.filter_department = department

    @rx.event
    def set_view_mode(self, mode: str):
        self.view_mode = mode

    @rx.event
    def open_detail_modal(self, employee: Employee):
        self.selected_employee = employee
        self.show_detail_modal = True

    @rx.event
    def close_detail_modal(self):
        self.show_detail_modal = False
        self.selected_employee = None

    @rx.event
    def open_add_modal(self):
        self.is_editing = False
        self.new_employee_data = {
            "id": 0,
            "name": "",
            "email": "",
            "phone": "",
            "role": "",
            "department": "Engineering",
            "hire_date": "",
            "salary": "",
            "is_active": True,
        }
        self.show_add_edit_modal = True

    @rx.event
    def open_edit_modal(self, employee: Employee):
        self.is_editing = True
        self.new_employee_data = employee
        self.close_detail_modal()
        self.show_add_edit_modal = True

    @rx.event
    def close_add_edit_modal(self):
        self.show_add_edit_modal = False

    def _set_new_employee_data(self, key: str, value: str | bool):
        self.new_employee_data[key] = value

    @rx.event
    def set_new_employee_field(self, field_data: list):
        self._set_new_employee_data(field_data[0], field_data[1])

    @rx.event
    def add_employee(self):
        new_id = max((e["id"] for e in self.employees)) + 1 if self.employees else 1
        self.new_employee_data["id"] = new_id
        self.employees.append(self.new_employee_data)
        self.close_add_edit_modal()

    @rx.event
    def edit_employee(self):
        if self.new_employee_data:
            index_to_update = -1
            for i, emp in enumerate(self.employees):
                if emp["id"] == self.new_employee_data["id"]:
                    index_to_update = i
                    break
            if index_to_update != -1:
                self.employees[index_to_update] = self.new_employee_data
        self.close_add_edit_modal()

    @rx.event
    def delete_employee(self, employee_id: int):
        self.employees = [e for e in self.employees if e["id"] != employee_id]
        self.close_detail_modal()