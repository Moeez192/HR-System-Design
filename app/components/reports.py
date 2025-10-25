import reflex as rx
from app.states.reports_state import ReportsState


def chart_card(title: str, chart: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-700 mb-4"),
        chart,
        class_name="p-6 bg-white rounded-lg shadow-sm border border-gray-200",
    )


def reports_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.h1("Analytics & Reports", class_name="text-2xl font-bold mb-6"),
            rx.el.div(
                chart_card(
                    "Headcount by Department",
                    rx.recharts.pie_chart(
                        rx.recharts.pie(
                            data_key="count",
                            name_key="department",
                            data=ReportsState.headcount_by_department,
                            cx="50%",
                            cy="50%",
                            outer_radius=80,
                            fill="#8884d8",
                            label=True,
                            stroke="#fff",
                            stroke_width=2,
                        ),
                        rx.recharts.tooltip(),
                        width="100%",
                        height=300,
                    ),
                ),
                chart_card(
                    "Leave Trends",
                    rx.recharts.bar_chart(
                        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                        rx.recharts.x_axis(data_key="month"),
                        rx.recharts.y_axis(),
                        rx.recharts.tooltip(),
                        rx.recharts.bar(data_key="Sick", fill="#FBBF24"),
                        rx.recharts.bar(data_key="Vacation", fill="#3B82F6"),
                        rx.recharts.bar(data_key="Personal", fill="#8B5CF6"),
                        data=ReportsState.leave_trends,
                        width="100%",
                        height=300,
                    ),
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6",
            ),
            chart_card(
                "Payroll Summary",
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Employee",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Base Salary",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Bonus",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                                rx.el.th(
                                    "Total Pay",
                                    class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                ReportsState.payroll_summary,
                                lambda row: rx.el.tr(
                                    rx.el.td(
                                        row["name"],
                                        class_name="px-6 py-4 whitespace-nowrap text-sm",
                                    ),
                                    rx.el.td(
                                        row["base_salary"],
                                        class_name="px-6 py-4 whitespace-nowrap text-sm",
                                    ),
                                    rx.el.td(
                                        row["bonus"],
                                        class_name="px-6 py-4 whitespace-nowrap text-sm",
                                    ),
                                    rx.el.td(
                                        row["total"],
                                        class_name="px-6 py-4 whitespace-nowrap text-sm",
                                    ),
                                ),
                            ),
                            class_name="bg-white divide-y divide-gray-200",
                        ),
                        class_name="min-w-full divide-y divide-gray-200",
                    ),
                    class_name="shadow overflow-x-auto border-b border-gray-200 sm:rounded-lg",
                ),
            ),
        ),
        class_name="flex-1 p-6",
    )