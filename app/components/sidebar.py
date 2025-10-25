import reflex as rx


def nav_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=href,
        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.icon("mountain", class_name="h-6 w-6"),
                rx.el.span("HR Flow", class_name="sr-only"),
                href="#",
                class_name="flex h-14 items-center justify-center rounded-lg bg-gray-100 lg:h-[60px]",
            ),
            rx.el.nav(
                nav_item("Dashboard", "home", "#"),
                nav_item("Employees", "users", "/"),
                nav_item("Leave", "calendar-days", "/leave"),
                nav_item("Attendance", "clipboard-check", "/attendance"),
                nav_item("Reports", "bar-chart-3", "/reports"),
                class_name="grid gap-2 text-sm font-medium",
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="hidden border-r bg-gray-100/40 lg:block",
    )