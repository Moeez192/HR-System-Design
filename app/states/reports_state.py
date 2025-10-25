import reflex as rx
from typing import TypedDict, Any
from collections import Counter
import datetime


class HeadcountData(TypedDict):
    department: str
    count: int


class LeaveTrendData(TypedDict):
    month: str
    Sick: int
    Vacation: int
    Personal: int


class AttendanceOverviewData(TypedDict):
    name: str
    value: int


class PayrollSummaryData(TypedDict):
    name: str
    department: str
    role: str
    base_salary: str
    bonus: str
    total: str


class ReportsState(rx.State):
    headcount_by_department: list[HeadcountData] = []
    leave_trends: list[LeaveTrendData] = []
    attendance_overview: list[AttendanceOverviewData] = []
    payroll_summary: list[PayrollSummaryData] = []

    @rx.event
    async def load_report_data(self):
        from app.states.employee_state import EmployeeState
        from app.states.leave_state import LeaveState
        from app.states.attendance_state import AttendanceState

        employee_state = await self.get_state(EmployeeState)
        leave_state = await self.get_state(LeaveState)
        attendance_state = await self.get_state(AttendanceState)
        if not employee_state.employees:
            await employee_state.load_employees()
        if not leave_state.leave_requests:
            leave_state.load_requests()
        if not attendance_state.attendance_records:
            attendance_state.load_attendance()
        dept_counts = Counter((e["department"] for e in employee_state.employees))
        self.headcount_by_department = [
            {"department": dept, "count": count} for dept, count in dept_counts.items()
        ]
        leave_trends_data: dict[str, Counter] = {}
        for req in leave_state.leave_requests:
            month = datetime.datetime.fromisoformat(req["start_date"]).strftime("%b %Y")
            if month not in leave_trends_data:
                leave_trends_data[month] = Counter()
            leave_trends_data[month][req["leave_type"]] += 1
        self.leave_trends = []
        for month, counts in sorted(leave_trends_data.items()):
            self.leave_trends.append(
                {
                    "month": month,
                    "Sick": counts.get("Sick", 0),
                    "Vacation": counts.get("Vacation", 0),
                    "Personal": counts.get("Personal", 0),
                }
            )
        attendance_counts = Counter(
            (a["status"] for a in attendance_state.attendance_records)
        )
        self.attendance_overview = [
            {"name": status, "value": count}
            for status, count in attendance_counts.items()
        ]
        self.payroll_summary = []
        for emp in employee_state.employees:
            salary_val = int(emp["salary"].replace("$", "").replace(",", ""))
            bonus_val = salary_val * 0.1
            total_val = salary_val + bonus_val
            self.payroll_summary.append(
                {
                    "name": emp["name"],
                    "department": emp["department"],
                    "role": emp["role"],
                    "base_salary": f"${salary_val:,.2f}",
                    "bonus": f"${bonus_val:,.2f}",
                    "total": f"${total_val:,.2f}",
                }
            )