import reflex as rx
from typing import TypedDict, Literal
import datetime

LeaveStatus = Literal["Pending", "Approved", "Rejected"]
LeaveType = Literal["Sick", "Vacation", "Personal", "Unpaid"]


class LeaveRequest(TypedDict):
    id: int
    employee_id: int
    employee_name: str
    leave_type: LeaveType
    start_date: str
    end_date: str
    reason: str
    status: LeaveStatus
    request_date: str


class LeaveState(rx.State):
    leave_requests: list[LeaveRequest] = []
    show_request_modal: bool = False
    new_request_data: dict = {
        "leave_type": "Sick",
        "start_date": "",
        "end_date": "",
        "reason": "",
    }
    filter_status: str = "All"

    @rx.event
    def load_requests(self):
        self.leave_requests = [
            {
                "id": 1,
                "employee_id": 1,
                "employee_name": "Alice Johnson",
                "leave_type": "Vacation",
                "start_date": "2024-08-01",
                "end_date": "2024-08-05",
                "reason": "Family trip",
                "status": "Approved",
                "request_date": "2024-07-15",
            },
            {
                "id": 2,
                "employee_id": 2,
                "employee_name": "Bob Smith",
                "leave_type": "Sick",
                "start_date": "2024-07-20",
                "end_date": "2024-07-21",
                "reason": "Flu",
                "status": "Approved",
                "request_date": "2024-07-20",
            },
            {
                "id": 3,
                "employee_id": 3,
                "employee_name": "Charlie Brown",
                "leave_type": "Personal",
                "start_date": "2024-08-10",
                "end_date": "2024-08-10",
                "reason": "Appointment",
                "status": "Pending",
                "request_date": "2024-07-22",
            },
            {
                "id": 4,
                "employee_id": 5,
                "employee_name": "Ethan Hunt",
                "leave_type": "Vacation",
                "start_date": "2024-09-01",
                "end_date": "2024-09-10",
                "reason": "Extended holiday",
                "status": "Pending",
                "request_date": "2024-07-20",
            },
            {
                "id": 5,
                "employee_id": 4,
                "employee_name": "Diana Prince",
                "leave_type": "Sick",
                "start_date": "2024-07-18",
                "end_date": "2024-07-19",
                "reason": "Migraine",
                "status": "Rejected",
                "request_date": "2024-07-18",
            },
        ]

    @rx.var
    def filtered_requests(self) -> list[LeaveRequest]:
        if self.filter_status == "All":
            return self.leave_requests
        return [
            req for req in self.leave_requests if req["status"] == self.filter_status
        ]

    @rx.event
    def open_request_modal(self):
        self.new_request_data = {
            "leave_type": "Sick",
            "start_date": datetime.date.today().isoformat(),
            "end_date": datetime.date.today().isoformat(),
            "reason": "",
        }
        self.show_request_modal = True

    @rx.event
    def close_request_modal(self):
        self.show_request_modal = False

    def _set_new_request_data(self, key: str, value: str):
        self.new_request_data[key] = value

    @rx.event
    def set_new_request_field(self, field_data: list):
        self._set_new_request_data(field_data[0], field_data[1])

    @rx.event
    def submit_request(self, form_data: dict):
        new_id = (
            max((r["id"] for r in self.leave_requests)) + 1
            if self.leave_requests
            else 1
        )
        request: LeaveRequest = {
            "id": new_id,
            "employee_id": 1,
            "employee_name": "Alice Johnson",
            "leave_type": form_data.get(
                "leave_type", self.new_request_data["leave_type"]
            ),
            "start_date": form_data.get(
                "start_date", self.new_request_data["start_date"]
            ),
            "end_date": form_data.get("end_date", self.new_request_data["end_date"]),
            "reason": form_data.get("reason", self.new_request_data["reason"]),
            "status": "Pending",
            "request_date": datetime.date.today().isoformat(),
        }
        self.leave_requests.append(request)
        self.close_request_modal()

    @rx.event
    def update_request_status(self, request_id: int, status: LeaveStatus):
        for i, req in enumerate(self.leave_requests):
            if req["id"] == request_id:
                self.leave_requests[i]["status"] = status
                break