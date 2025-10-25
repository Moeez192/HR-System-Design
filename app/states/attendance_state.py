import reflex as rx
from typing import TypedDict, Literal
import datetime

AttendanceStatus = Literal["On Time", "Late", "Absent", "Checked Out"]


class AttendanceRecord(TypedDict):
    id: int
    employee_id: int
    employee_name: str
    date: str
    check_in_time: str | None
    check_out_time: str | None
    status: AttendanceStatus


class AttendanceState(rx.State):
    attendance_records: list[AttendanceRecord] = []
    filter_date: str = ""
    filter_status: str = "All"
    current_check_in_status: dict[int, str] = {}

    @rx.event
    def load_attendance(self):
        if not self.attendance_records:
            self.attendance_records = [
                {
                    "id": 1,
                    "employee_id": 1,
                    "employee_name": "Alice Johnson",
                    "date": "2024-07-28",
                    "check_in_time": "09:05",
                    "check_out_time": "17:30",
                    "status": "On Time",
                },
                {
                    "id": 2,
                    "employee_id": 2,
                    "employee_name": "Bob Smith",
                    "date": "2024-07-28",
                    "check_in_time": "09:15",
                    "check_out_time": "17:45",
                    "status": "Late",
                },
                {
                    "id": 3,
                    "employee_id": 3,
                    "employee_name": "Charlie Brown",
                    "date": "2024-07-28",
                    "check_in_time": None,
                    "check_out_time": None,
                    "status": "Absent",
                },
                {
                    "id": 4,
                    "employee_id": 4,
                    "employee_name": "Diana Prince",
                    "date": "2024-07-28",
                    "check_in_time": "08:55",
                    "check_out_time": "17:00",
                    "status": "Checked Out",
                },
                {
                    "id": 5,
                    "employee_id": 5,
                    "employee_name": "Ethan Hunt",
                    "date": "2024-07-28",
                    "check_in_time": "09:00",
                    "check_out_time": None,
                    "status": "On Time",
                },
            ]

    @rx.event
    def check_in(self, employee_id: int):
        now = datetime.datetime.now()
        status: AttendanceStatus = (
            "Late" if now.hour > 9 or (now.hour == 9 and now.minute > 5) else "On Time"
        )
        new_record = {
            "id": len(self.attendance_records) + 1,
            "employee_id": employee_id,
            "employee_name": f"Employee {employee_id}",
            "date": now.strftime("%Y-%m-%d"),
            "check_in_time": now.strftime("%H:%M"),
            "check_out_time": None,
            "status": status,
        }
        self.attendance_records.append(new_record)
        self.current_check_in_status[employee_id] = "Checked In"

    @rx.event
    def check_out(self, employee_id: int):
        now = datetime.datetime.now().strftime("%H:%M")
        today = datetime.date.today().isoformat()
        for i, record in enumerate(self.attendance_records):
            if record["employee_id"] == employee_id and record["date"] == today:
                self.attendance_records[i]["check_out_time"] = now
                self.attendance_records[i]["status"] = "Checked Out"
                break
        del self.current_check_in_status[employee_id]

    @rx.var
    def filtered_attendance(self) -> list[AttendanceRecord]:
        records = self.attendance_records
        if self.filter_date and self.filter_date != "":
            records = [r for r in records if r["date"] == self.filter_date]
        if self.filter_status != "All":
            records = [r for r in records if r["status"] == self.filter_status]
        return records

    @rx.event
    def set_filter_date(self, date: str):
        self.filter_date = date

    @rx.event
    def set_filter_status(self, status: str):
        self.filter_status = status