import reflex as rx
from app.states.employee_state import EmployeeState
from app.states.leave_state import LeaveState
from app.states.attendance_state import AttendanceState
from app.states.reports_state import ReportsState
from app.components.sidebar import sidebar
from app.components.employee_directory import employee_directory_page
from app.components.leave_management import leave_management_page
from app.components.attendance_tracking import attendance_tracking_page
from app.components.reports import reports_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        employee_directory_page(),
        class_name="grid min-h-screen w-full lg:grid-cols-[280px_1fr]",
    )


def leave() -> rx.Component:
    return rx.el.div(
        sidebar(),
        leave_management_page(),
        class_name="grid min-h-screen w-full lg:grid-cols-[280px_1fr]",
    )


def attendance() -> rx.Component:
    return rx.el.div(
        sidebar(),
        attendance_tracking_page(),
        class_name="grid min-h-screen w-full lg:grid-cols-[280px_1fr]",
    )


def reports() -> rx.Component:
    return rx.el.div(
        sidebar(),
        reports_page(),
        class_name="grid min-h-screen w-full lg:grid-cols-[280px_1fr]",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, on_load=EmployeeState.load_employees)
app.add_page(leave, on_load=LeaveState.load_requests)
app.add_page(attendance, route="/attendance", on_load=AttendanceState.load_attendance)
app.add_page(reports, on_load=ReportsState.load_report_data)