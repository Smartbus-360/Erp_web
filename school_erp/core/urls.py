from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # Dashboard
    path("login/", views.login_view, name="login"),
path("logout/", views.logout_view, name="logout"),

    path("", views.dashboard, name="dashboard"),

    # ---------------- General Settings ----------------
    path("settings/institute-profile/", views.institute_profile, name="institute_profile"),
    path("settings/fee-particulars/", views.fee_particulars, name="fee_particulars"),
    path("settings/accounts-invoice/", views.accounts_invoice, name="accounts_invoice"),
    path("settings/rules-regulations/", views.rules_regulations, name="rules_regulations"),
    path("settings/marks-grading/", views.marks_grading, name="marks_grading"),
    path("settings/account-settings/", views.account_settings, name="account_settings"),

    # ---------------- Classes ----------------
    path("classes/", views.all_classes, name="all_classes"),
    path("classes/new/", views.new_class, name="new_class"),

    # ---------------- Subjects ----------------
    path("subjects/classes/", views.classes_with_subjects, name="classes_with_subjects"),
    path("subjects/assign/", views.assign_subjects, name="assign_subjects"),

    # ---------------- Students ----------------
    path("students/", views.all_students, name="all_students"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/admission-letter/", views.admission_letter, name="admission_letter"),
path("students/admission-letter/print/<int:student_id>/", views.print_admission_letter, name="print_admission_letter"),
path(
    "students/id-cards/",
    views.student_id_cards,
    name="student_id_cards"
),
path(
    "students/print-basic-list/",
    views.print_basic_list,
    name="print_basic_list"
),
path(
    "students/manage-login/",
    views.manage_login,
    name="manage_login"
),
path(
    "students/promote/",
    views.promote_students,
    name="promote_students"
),
path(
    "employees/",
    views.all_employees,
    name="all_employees"
),
path(
    "employees/add/",
    views.add_employee,
    name="add_employee"
),
path(
    "employees/job-letter/",
    views.job_letter_search,
    name="job_letter"
),
path(
    "employees/job-letter/<int:employee_id>/",
    views.job_letter_preview,
    name="job_letter_preview"
),
path(
    "employees/job-letter/<int:employee_id>/print/",
    views.job_letter_print,
    name="job_letter_print"
),
path(
    "employees/manage-login/",
    views.employee_manage_login,
    name="employee_manage_login"
),
path(
    "accounts/chart-of-accounts/",
    views.chart_of_accounts,
    name="chart_of_accounts"
),
path(
    "accounts/add-income/",
    views.add_income,
    name="add_income"
),
path(
    "accounts/add-expense/",
    views.add_expense,
    name="add_expense"
),
path(
    "accounts/account-statement/",
    views.account_statement,
    name="account_statement"
),
# Fees
path('fees/generate/', views.generate_fees_invoice, name='generate_fees'),
path('fees/invoice-preview/', views.fees_invoice_preview, name='fees_invoice_preview'),
path(
    "fees/collect-fees/",
    views.collect_fees_search,
    name="collect_fees"
),

path(
    "fees/collect-fees/form/",
    views.collect_fees_form,
    name="collect_fees_form"
),
# Fees Paid Slip
path(
    "fees/paid-slip/",
    views.fees_paid_slip_search,
    name="fees_paid_slip"
),

path(
    "fees/paid-slip/receipt/",
    views.fees_paid_receipt,
    name="fees_paid_receipt"
),
path(
    "fees/defaulters/",
    views.fees_defaulters,
    name="fees_defaulters"
),
# Salary
path(
    "salary/pay/",
    views.pay_salary_search,
    name="pay_salary"
),

path(
    "salary/pay/<int:employee_id>/",
    views.pay_salary_form,
    name="pay_salary_form"
),
# Salary

# Attendance
path(
    "attendance/students/",
    views.students_attendance_search,
    name="students_attendance"
),

path(
    "attendance/students/sheet/",
    views.students_attendance_sheet,
    name="students_attendance_sheet"
),
# Employees Attendance
path(
    "attendance/employees/",
    views.employees_attendance_search,
    name="employees_attendance"
),

path(
    "attendance/employees/sheet/",
    views.employees_attendance_sheet,
    name="employees_attendance_sheet"
),
path(
    "attendance/class-wise-report/",
    views.class_wise_report,
    name="class_wise_report"
),
path(
    "attendance/employees-attendance-report/",
    views.employees_attendance_report,
    name="employees_attendance_report"
),
path(
    "attendance/students-attendance-report/",
    views.students_attendance_report,
    name="students_attendance_report"
),
# ---------------- Homework ----------------
path(
    "homework/",
    views.homework_list,
    name="homework_list"
),
# Exams
path(
    "exams/create/",
    views.create_exam,
    name="create_exam"
),
# Exam Marks

# Result Card

path('class_tests/manage-test-marks/', views.manage_test_marks, name='manage_test_marks'),
    path('class_tests/test-result/', views.test_result, name='test_result'),
path(
    "class-tests/test-results/",
    views.class_test_results,
    name="class_test_results"
),
path(
    "students/promotion-history/",
    views.promotion_history,
    name="promotion_history"
),
path("syllabus/view/", views.view_syllabus, name="view_syllabus"),
path("timetable/weekdays/", views.timetable_weekdays, name="timetable_weekdays"),
path("timetable/periods/", views.timetable_periods, name="timetable_periods"),
path("timetable/class/", views.timetable_class, name="timetable_class"),
path("timetable/print/", views.timetable_print, name="timetable_print"),
path("timetable/teacher/", views.timetable_teacher, name="timetable_teacher"),

path(
    "exams/<int:exam_id>/schedule/",
    views.exam_schedule,
    name="exam_schedule"
),
path(
    "fees/fine-settings/",
    views.fee_fine_settings,
    name="fee_fine_settings"
),
# urls.py
path("salary-slip/", views.salary_slip_page, name="salary_paid_slip"),
path("messages/", views.messaging_home, name="messages_home"),
path("messages/inbox/", views.messages_inbox, name="messages_inbox"),
path("messages/compose/", views.messages_compose, name="messages_compose"),
path("messages/<int:message_id>/", views.view_message, name="view_message"),
path(
    "classes/<int:class_id>/sections/",
    views.class_sections,
    name="class_sections"
),
path("employees/profile/", views.employee_profile, name="employee_profile")


]
