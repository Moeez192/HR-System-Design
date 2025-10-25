import reflex as rx
from app.states.employee_state import EmployeeState, Employee
from typing import Any


def employee_card(employee: Employee) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=f"https://api.dicebear.com/9.x/initials/svg?seed={employee['name']}",
                alt=employee["name"],
                class_name="rounded-full w-20 h-20 object-cover mx-auto",
            ),
            rx.el.h3(
                employee["name"], class_name="mt-4 text-lg font-semibold text-gray-900"
            ),
            rx.el.p(employee["role"], class_name="text-sm text-gray-500"),
            rx.el.p(employee["department"], class_name="text-xs text-gray-400"),
            class_name="text-center",
        ),
        on_click=lambda: EmployeeState.open_detail_modal(employee),
        class_name="p-4 bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-lg transition-shadow cursor-pointer",
    )


def employee_list_item(employee: Employee) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={employee['name']}",
                    alt=employee["name"],
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p(employee["name"], class_name="font-medium text-gray-900"),
                    rx.el.p(employee["email"], class_name="text-sm text-gray-500"),
                    class_name="ml-4",
                ),
                class_name="flex items-center",
            ),
            class_name="whitespace-nowrap px-6 py-4",
        ),
        rx.el.td(
            employee["role"], class_name="whitespace-nowrap px-6 py-4 text-gray-700"
        ),
        rx.el.td(
            employee["department"],
            class_name="whitespace-nowrap px-6 py-4 text-gray-700",
        ),
        rx.el.td(
            rx.el.span(
                rx.cond(employee["is_active"], "Active", "Inactive"),
                class_name=rx.cond(
                    employee["is_active"],
                    "bg-green-100 text-green-800",
                    "bg-red-100 text-red-800",
                )
                + " px-2 inline-flex text-xs leading-5 font-semibold rounded-full w-fit",
            ),
            class_name="whitespace-nowrap px-6 py-4",
        ),
        on_click=lambda: EmployeeState.open_detail_modal(employee),
        class_name="hover:bg-gray-50 cursor-pointer",
    )


def employee_detail_modal() -> rx.Component:
    return rx.el.div(
        rx.cond(
            EmployeeState.show_detail_modal,
            rx.el.div(
                rx.el.div(class_name="fixed inset-0 bg-black/30 z-40"),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "Employee Details",
                                    class_name="text-lg font-medium leading-6 text-gray-900",
                                ),
                                rx.el.button(
                                    rx.icon("x", class_name="h-4 w-4"),
                                    on_click=EmployeeState.close_detail_modal,
                                    class_name="p-1 rounded-full hover:bg-gray-200",
                                ),
                                class_name="flex items-center justify-between p-4 border-b",
                            ),
                            rx.cond(
                                EmployeeState.selected_employee,
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.img(
                                            src=f"https://api.dicebear.com/9.x/initials/svg?seed={EmployeeState.selected_employee['name']}",
                                            class_name="h-24 w-24 rounded-full mx-auto",
                                        ),
                                        rx.el.h4(
                                            EmployeeState.selected_employee["name"],
                                            class_name="text-center mt-4 text-xl font-bold",
                                        ),
                                        rx.el.p(
                                            EmployeeState.selected_employee["role"],
                                            class_name="text-center text-gray-500",
                                        ),
                                        class_name="py-5",
                                    ),
                                    rx.el.div(
                                        rx.el.dl(
                                            rx.el.div(
                                                rx.el.dt(
                                                    "Department",
                                                    class_name="font-medium text-gray-500",
                                                ),
                                                rx.el.dd(
                                                    EmployeeState.selected_employee[
                                                        "department"
                                                    ],
                                                    class_name="mt-1 text-gray-900",
                                                ),
                                                class_name="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6",
                                            ),
                                            rx.el.div(
                                                rx.el.dt(
                                                    "Email",
                                                    class_name="font-medium text-gray-500",
                                                ),
                                                rx.el.dd(
                                                    EmployeeState.selected_employee[
                                                        "email"
                                                    ],
                                                    class_name="mt-1 text-gray-900",
                                                ),
                                                class_name="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6",
                                            ),
                                            rx.el.div(
                                                rx.el.dt(
                                                    "Phone",
                                                    class_name="font-medium text-gray-500",
                                                ),
                                                rx.el.dd(
                                                    EmployeeState.selected_employee[
                                                        "phone"
                                                    ],
                                                    class_name="mt-1 text-gray-900",
                                                ),
                                                class_name="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6",
                                            ),
                                            rx.el.div(
                                                rx.el.dt(
                                                    "Hire Date",
                                                    class_name="font-medium text-gray-500",
                                                ),
                                                rx.el.dd(
                                                    EmployeeState.selected_employee[
                                                        "hire_date"
                                                    ],
                                                    class_name="mt-1 text-gray-900",
                                                ),
                                                class_name="bg-gray-50 px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6",
                                            ),
                                            rx.el.div(
                                                rx.el.dt(
                                                    "Salary",
                                                    class_name="font-medium text-gray-500",
                                                ),
                                                rx.el.dd(
                                                    EmployeeState.selected_employee[
                                                        "salary"
                                                    ],
                                                    class_name="mt-1 text-gray-900",
                                                ),
                                                class_name="px-4 py-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6",
                                            ),
                                        ),
                                        class_name="border-t border-gray-200",
                                    ),
                                    rx.el.div(
                                        rx.el.button(
                                            rx.icon(
                                                "trash-2", class_name="mr-2 h-4 w-4"
                                            ),
                                            "Delete",
                                            on_click=lambda: EmployeeState.delete_employee(
                                                EmployeeState.selected_employee["id"]
                                            ),
                                            class_name="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 text-destructive-foreground h-10 px-4 py-2 bg-red-600 text-white hover:bg-red-700 rounded-md",
                                        ),
                                        rx.el.button(
                                            rx.icon(
                                                "pencil", class_name="mr-2 h-4 w-4"
                                            ),
                                            "Edit",
                                            on_click=lambda: EmployeeState.open_edit_modal(
                                                EmployeeState.selected_employee
                                            ),
                                            class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2",
                                        ),
                                        class_name="flex items-center justify-end gap-2 p-4 border-t",
                                    ),
                                    class_name="overflow-y-auto max-h-[70vh]",
                                ),
                                rx.el.div("No employee selected.", class_name="p-6"),
                            ),
                        ),
                        class_name="bg-white rounded-lg shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full",
                    ),
                    class_name="fixed inset-0 z-50 overflow-y-auto flex items-center justify-center p-4",
                ),
            ),
        )
    )


def employee_directory_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Employee Directory", class_name="text-2xl font-bold"),
                rx.el.div(
                    rx.el.input(
                        placeholder="Search employees...",
                        on_change=EmployeeState.set_search_query.debounce(300),
                        class_name="w-full md:w-64 px-4 py-2 border rounded-lg",
                    ),
                    rx.el.select(
                        rx.foreach(
                            EmployeeState.department_options,
                            lambda dept: rx.el.option(dept, value=dept),
                        ),
                        on_change=EmployeeState.set_filter_department,
                        class_name="border rounded-lg px-4 py-2",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("layout-grid", class_name="h-5 w-5"),
                            on_click=lambda: EmployeeState.set_view_mode("grid"),
                            class_name=rx.cond(
                                EmployeeState.view_mode == "grid", "bg-gray-200", ""
                            )
                            + " p-2 rounded-l-lg",
                        ),
                        rx.el.button(
                            rx.icon("list", class_name="h-5 w-5"),
                            on_click=lambda: EmployeeState.set_view_mode("list"),
                            class_name=rx.cond(
                                EmployeeState.view_mode == "list", "bg-gray-200", ""
                            )
                            + " p-2 rounded-r-lg",
                        ),
                        class_name="flex border rounded-lg overflow-hidden",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="mr-2 h-4 w-4"),
                        "Add Employee",
                        on_click=EmployeeState.open_add_modal,
                        class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-blue-600 text-white hover:bg-blue-700 h-10 px-4 py-2",
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.cond(
                EmployeeState.view_mode == "grid",
                rx.el.div(
                    rx.foreach(EmployeeState.filtered_employees, employee_card),
                    class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6",
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
                                    "Role",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Department",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Status",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                EmployeeState.filtered_employees, employee_list_item
                            ),
                            class_name="bg-white divide-y divide-gray-200",
                        ),
                        class_name="min-w-full divide-y divide-gray-200",
                    ),
                    class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
                ),
            ),
        ),
        add_edit_employee_modal(),
        employee_detail_modal(),
        class_name="flex-1 p-6",
    )


def form_field(
    label: str, name: str, value: rx.Var[str | bool], type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700"),
        rx.el.input(
            type=type,
            default_value=value,
            on_change=lambda val: EmployeeState.set_new_employee_field([name, val]),
            class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm",
        ),
        class_name="col-span-1",
    )


def add_edit_employee_modal() -> rx.Component:
    return rx.el.div(
        rx.cond(
            EmployeeState.show_add_edit_modal,
            rx.el.div(
                rx.el.div(class_name="fixed inset-0 bg-black/30 z-40"),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                rx.cond(
                                    EmployeeState.is_editing,
                                    "Edit Employee",
                                    "Add Employee",
                                ),
                                class_name="text-lg font-medium leading-6 text-gray-900",
                            ),
                            rx.el.button(
                                rx.icon("x", class_name="h-4 w-4"),
                                on_click=EmployeeState.close_add_edit_modal,
                                class_name="p-1 rounded-full hover:bg-gray-200",
                            ),
                            class_name="flex items-center justify-between p-4 border-b",
                        ),
                        rx.el.div(
                            form_field(
                                "Name", "name", EmployeeState.new_employee_data["name"]
                            ),
                            form_field(
                                "Email",
                                "email",
                                EmployeeState.new_employee_data["email"],
                                type="email",
                            ),
                            form_field(
                                "Phone",
                                "phone",
                                EmployeeState.new_employee_data["phone"],
                                type="tel",
                            ),
                            form_field(
                                "Role", "role", EmployeeState.new_employee_data["role"]
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Department",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.select(
                                    rx.foreach(
                                        EmployeeState.department_options,
                                        lambda dept: rx.cond(
                                            dept != "All",
                                            rx.el.option(dept, value=dept),
                                            None,
                                        ),
                                    ),
                                    value=EmployeeState.new_employee_data["department"],
                                    on_change=lambda val: EmployeeState.set_new_employee_field(
                                        ["department", val]
                                    ),
                                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm",
                                ),
                                class_name="col-span-1",
                            ),
                            form_field(
                                "Hire Date",
                                "hire_date",
                                EmployeeState.new_employee_data["hire_date"],
                                type="date",
                            ),
                            form_field(
                                "Salary",
                                "salary",
                                EmployeeState.new_employee_data["salary"],
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Status",
                                    class_name="block text-sm font-medium text-gray-700",
                                ),
                                rx.el.div(
                                    rx.el.input(
                                        type="checkbox",
                                        checked=EmployeeState.new_employee_data[
                                            "is_active"
                                        ],
                                        on_change=lambda val: EmployeeState.set_new_employee_field(
                                            ["is_active", val]
                                        ),
                                        class_name="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500",
                                    ),
                                    rx.el.label(
                                        "Active",
                                        class_name="ml-2 block text-sm text-gray-900",
                                    ),
                                    class_name="flex items-center mt-1",
                                ),
                                class_name="col-span-1",
                            ),
                            class_name="p-6 grid grid-cols-1 gap-6 sm:grid-cols-2",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                on_click=EmployeeState.close_add_edit_modal,
                                class_name="inline-flex justify-center rounded-md border border-transparent bg-gray-200 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-300",
                            ),
                            rx.el.button(
                                rx.cond(
                                    EmployeeState.is_editing,
                                    "Save Changes",
                                    "Add Employee",
                                ),
                                on_click=rx.cond(
                                    EmployeeState.is_editing,
                                    EmployeeState.edit_employee,
                                    EmployeeState.add_employee,
                                ),
                                class_name="ml-3 inline-flex justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700",
                            ),
                            class_name="flex justify-end p-4 border-t",
                        ),
                        class_name="bg-white rounded-lg shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full",
                    ),
                    class_name="fixed inset-0 z-50 overflow-y-auto flex items-center justify-center p-4",
                ),
            ),
        )
    )