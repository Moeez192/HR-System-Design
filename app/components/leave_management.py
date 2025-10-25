import reflex as rx
from app.states.leave_state import LeaveState, LeaveRequest, LeaveType


def status_badge(status: str) -> rx.Component:
    color_map = {
        "Pending": "bg-yellow-100 text-yellow-800",
        "Approved": "bg-green-100 text-green-800",
        "Rejected": "bg-red-100 text-red-800",
    }
    return rx.el.span(
        status,
        class_name=f"{color_map.get(status.to_string(), 'bg-gray-100 text-gray-800')} px-2 inline-flex text-xs leading-5 font-semibold rounded-full w-fit",
    )


def leave_request_row(request: LeaveRequest) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            request["employee_name"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            rx.el.span(request["leave_type"]),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            f"{request['start_date']} to {request['end_date']}",
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            request["reason"],
            class_name="px-6 py-4 max-w-xs whitespace-nowrap overflow-hidden text-ellipsis text-sm text-gray-500",
        ),
        rx.el.td(
            status_badge(request["status"]),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.cond(
                request["status"] == "Pending",
                rx.el.div(
                    rx.el.button(
                        "Approve",
                        on_click=lambda: LeaveState.update_request_status(
                            request["id"], "Approved"
                        ),
                        class_name="text-green-600 hover:text-green-900",
                    ),
                    rx.el.button(
                        "Reject",
                        on_click=lambda: LeaveState.update_request_status(
                            request["id"], "Rejected"
                        ),
                        class_name="ml-4 text-red-600 hover:text-red-900",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.span("-", class_name="text-gray-500"),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def leave_request_modal() -> rx.Component:
    leave_types: list[LeaveType] = ["Sick", "Vacation", "Personal", "Unpaid"]
    return rx.el.div(
        rx.cond(
            LeaveState.show_request_modal,
            rx.el.div(
                rx.el.div(class_name="fixed inset-0 bg-black/30 z-40"),
                rx.el.div(
                    rx.el.form(
                        rx.el.div(
                            rx.el.h3(
                                "New Leave Request",
                                class_name="text-lg font-medium leading-6 text-gray-900",
                            ),
                            rx.el.button(
                                rx.icon("x", class_name="h-4 w-4"),
                                on_click=LeaveState.close_request_modal,
                                class_name="p-1 rounded-full hover:bg-gray-200",
                            ),
                            class_name="flex items-center justify-between p-4 border-b",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Leave Type",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.select(
                                    rx.foreach(
                                        leave_types,
                                        lambda lt: rx.el.option(lt, value=lt),
                                    ),
                                    value=LeaveState.new_request_data["leave_type"],
                                    on_change=lambda val: LeaveState.set_new_request_field(
                                        ["leave_type", val]
                                    ),
                                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Start Date",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.input(
                                    type="date",
                                    name="start_date",
                                    default_value=LeaveState.new_request_data[
                                        "start_date"
                                    ],
                                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "End Date",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.input(
                                    type="date",
                                    name="end_date",
                                    default_value=LeaveState.new_request_data[
                                        "end_date"
                                    ],
                                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Reason",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.textarea(
                                    default_value=LeaveState.new_request_data["reason"],
                                    on_change=lambda val: LeaveState.set_new_request_field(
                                        ["reason", val]
                                    ),
                                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm",
                                    rows=3,
                                ),
                                class_name="col-span-2",
                            ),
                            class_name="p-6 grid grid-cols-1 gap-6 sm:grid-cols-2",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                on_click=LeaveState.close_request_modal,
                                class_name="inline-flex justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50",
                            ),
                            rx.el.button(
                                "Submit Request",
                                on_click=LeaveState.submit_request,
                                class_name="ml-3 inline-flex justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700",
                            ),
                            class_name="flex justify-end p-4 border-t",
                        ),
                        on_submit=LeaveState.submit_request,
                        class_name="bg-white rounded-lg shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full",
                    ),
                    class_name="fixed inset-0 z-50 overflow-y-auto flex items-center justify-center p-4",
                ),
            ),
        )
    )


def leave_management_page() -> rx.Component:
    status_options = ["All", "Pending", "Approved", "Rejected"]
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Leave Management", class_name="text-2xl font-bold"),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(status_options, lambda s: rx.el.option(s, value=s)),
                        on_change=LeaveState.set_filter_status,
                        class_name="border rounded-lg px-4 py-2",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="mr-2 h-4 w-4"),
                        "Request Leave",
                        on_click=LeaveState.open_request_modal,
                        class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-blue-600 text-white hover:bg-blue-700 h-10 px-4 py-2",
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex items-center justify-between mb-6",
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
                                "Type",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Dates",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Reason",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                rx.el.span("Actions", class_name="sr-only"),
                                class_name="relative px-6 py-3",
                            ),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(LeaveState.filtered_requests, leave_request_row),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200",
                ),
                class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
            ),
        ),
        leave_request_modal(),
        class_name="flex-1 p-6",
    )