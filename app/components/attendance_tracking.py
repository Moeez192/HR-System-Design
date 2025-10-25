import reflex as rx
from app.states.attendance_state import AttendanceState, AttendanceRecord


def attendance_status_badge(status: str) -> rx.Component:
    color_map = {
        "On Time": "bg-green-100 text-green-800",
        "Late": "bg-yellow-100 text-yellow-800",
        "Absent": "bg-red-100 text-red-800",
        "Checked Out": "bg-blue-100 text-blue-800",
    }
    return rx.el.span(
        status,
        class_name=f"{color_map.get(status.to_string(), 'bg-gray-100 text-gray-800')} px-2 inline-flex text-xs leading-5 font-semibold rounded-full w-fit",
    )


def attendance_row(record: AttendanceRecord) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            record["employee_name"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            record["date"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.cond(record["check_in_time"], record["check_in_time"], "-"),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.cond(record["check_out_time"], record["check_out_time"], "-"),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            attendance_status_badge(record["status"]),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
    )


def attendance_tracking_page() -> rx.Component:
    status_options = ["All", "On Time", "Late", "Absent", "Checked Out"]
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Attendance Tracking", class_name="text-2xl font-bold"),
                rx.el.div(
                    rx.el.input(
                        type="date",
                        on_change=AttendanceState.set_filter_date,
                        class_name="border rounded-lg px-4 py-2",
                        placeholder="Filter by date",
                        default_value=AttendanceState.filter_date,
                    ),
                    rx.el.select(
                        rx.foreach(status_options, lambda s: rx.el.option(s, value=s)),
                        default_value=AttendanceState.filter_status,
                        on_change=AttendanceState.set_filter_status,
                        class_name="border rounded-lg px-4 py-2",
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.el.div(
                rx.el.h2(
                    "Today's Check-in/out", class_name="text-xl font-semibold mb-4"
                ),
                rx.el.div(
                    rx.el.button(
                        "Check In",
                        on_click=lambda: AttendanceState.check_in(1),
                        class_name="bg-green-500 text-white px-4 py-2 rounded-lg",
                    ),
                    rx.el.button(
                        "Check Out",
                        on_click=lambda: AttendanceState.check_out(1),
                        class_name="bg-red-500 text-white px-4 py-2 rounded-lg ml-4",
                    ),
                    class_name="mb-6",
                ),
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Employee",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Date",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Check-in",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Check-out",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(AttendanceState.filtered_attendance, attendance_row),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200",
                ),
                class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
            ),
        ),
        class_name="flex-1 p-6",
    )