import requests
from django.shortcuts import render,redirect
from functools import wraps
from core.utils.api import api_request



FASTAPI_BASE_URL = "https://erp.backend.smartbus360.com"
API_BASE = FASTAPI_BASE_URL

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            response = requests.post(
                f"{FASTAPI_BASE_URL}/auth/login",
                json={"email": email, "password": password},
                timeout=10
            )

            if response.status_code != 200:
                return render(request, "base/login.html", {
                    "error": "Invalid credentials"
                })

            data = response.json()
            print("LOGIN RESPONSE:", data)

            # 🔐 Reset session
            request.session.flush()

            # ✅ STORE EXACTLY WHAT FASTAPI RETURNS
            request.session["auth"] = {
                "access_token": data.get("access_token"),
                "role": data.get("role"),
                "institute_id": data.get("institute_id"),
            }

            return redirect("core:dashboard")

        except requests.exceptions.RequestException:
            return render(request, "base/login.html", {
                "error": "Backend not reachable"
            })

    return render(request, "base/login.html")


# ---------------- Dashboard ----------------
# def dashboard(request):
#     return render(request, "dashboard/dashboard.html")
def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get("auth"):
            return redirect("core:login")
        return view_func(request, *args, **kwargs)
    return wrapper


def auth_context(request):
    auth = request.session.get("auth")
    return {
        "ACCESS_TOKEN": auth.get("access_token") if auth else ""
    }

def role_required(*allowed_roles):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            auth = request.session.get("auth")
            if not auth or auth.get("role") not in allowed_roles:
                return redirect("core:dashboard")
            return view(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


# ---------------- General Settings ----------------
def institute_profile(request):
    return render(request, "general_settings/institute_profile.html")

def fee_particulars(request):
    fee_items = [
        "MONTHLY TUITION FEE",
        "ADMISSION FEE",
        "REGISTRATION FEE",
        "ART MATERIAL",
        "TRANSPORT",
        "BOOKS",
        "UNIFORM",
        "FINE",
        "OTHERS",
    ]
    return render(
        request,
        "general_settings/fee_particulars.html",
        {"fee_items": fee_items},
    )

def accounts_invoice(request):
    return render(request, "general_settings/accounts_invoice.html")

def rules_regulations(request):
    return render(request, "general_settings/rules_regulations.html")

def marks_grading(request):
    grades = ["A+", "A", "B+", "B", "C", "D", "F"]
    return render(
        request,
        "general_settings/marks_grading.html",
        {"grades": grades},
    )

def account_settings(request):
    return render(request, "general_settings/account_settings.html")


# ---------------- Classes ----------------
def all_classes(request):
    return render(request, "classes/all_classes.html")

def new_class(request):
    return render(request, "classes/new_class.html")
@login_required
def class_sections(request, class_id):
    return render(
        request,
        "classes/class_sections.html",
        {
            "class_id": class_id
        }
    )


# ---------------- Subjects ----------------
def classes_with_subjects(request):
    return render(request, "subjects/classes_with_subjects.html")


def assign_subjects(request):
    return render(request, "subjects/assign_subjects.html")

def employee_profile(request):
    return render(request, "employees/employee_profile.html")


# ---------------- Students ----------------
def all_students(request):
    auth = request.session.get("auth")

    if not auth or "access_token" not in auth:
        return redirect("core:login")

    return render(
        request,
        "students/all_students.html",
        {
            "access_token": auth["access_token"]
        }
    )

def add_student(request):
    return render(request, "students/add_student.html")

def admission_letter(request):
    return render(request, "students/admission_letter.html")

def print_admission_letter(request, student_id):
    return render(request, "students/admission_letter_print.html")
def student_id_cards(request):
    return render(request, "students/student_id_cards.html")

def print_basic_list(request):
    return render(request, "students/print_basic_list.html")
def manage_login(request):
    return render(request, "students/manage_login.html")
def promote_students(request):
    return render(request, "students/promote_students.html")
def all_employees(request):
    return render(request, "employees/all_employees.html")
def add_employee(request):
    return render(request, "employees/add_employee.html")
# def job_letter(request):
#     return render(request, "employees/job_letter.html")
def job_letter_search(request):
    return render(request, "employees/job_letter_search.html")


def job_letter_preview(request, employee_id):
    return render(request, "employees/job_letter_preview.html", {
        "employee_id": employee_id
    })

def job_letter_print(request, employee_id):
    return render(request, "employees/job_letter_print.html", {
        "employee_id": employee_id
    })

def employee_manage_login(request):
    return render(request, "employees/manage_login.html")

def chart_of_accounts(request):
    return render(request, "accounts/chart_of_accounts.html")

def add_income(request):
    return render(request, "accounts/add_income.html")
def add_expense(request):
    return render(request, "accounts/add_expense.html")
def account_statement(request):
    return render(request, "accounts/account_statement.html")
def generate_fees_invoice(request):
    return render(request, 'fees/fees_generate.html')

def fees_invoice_preview(request):
    return render(request, 'fees/fees_invoice_preview.html')

# def collect_fees_search(request):
#     return render(request, "fees/collect_fees_search.html")
def collect_fees_search(request):
    return render(request, "fees/collect_fees_search.html")

def collect_fees_form(request):
    return render(request, "fees/collect_fees_form.html")
# ---------------- Fees Paid Slip ----------------
def fees_paid_slip_search(request):
    return render(request, "fees/fees_paid_slip_search.html")

def fees_paid_receipt(request):
    return render(request, "fees/fees_paid_receipt.html")
def fees_defaulters(request):
    return render(request, "fees/fees_defaulters.html")



# ---------------- Salary ----------------
def pay_salary_search(request):
    return render(request, "salary/pay_salary_search.html")

def pay_salary_form(request, employee_id):
    return render(request, "salary/pay_salary_form.html", {
        "employee_id": employee_id
    })
# ---------------- Salary ----------------


# ---------------- Employees Attendance ----------------
def employees_attendance_search(request):
    return render(request, "attendance/employees_attendance_search.html")

# def employees_attendance_sheet(request):
#     return render(request, "attendance/employees_attendance_sheet.html")
# ---------------- Class Wise Attendance Report ----------------

# ---------------- Employees Attendance Report ----------------

# ---------------- Students Attendance Report ----------------
# def students_attendance_report(request):
#     return render(
#         request,
#         "attendance/students_attendance_report.html"
#     )
# ---------------- Homework ----------------
def homework_list(request):
    return render(request, "homework/homework_list.html")
# ---------------- Exams ----------------
# ---------------- Exam Marks ----------------
# ---------------- Result Card ----------------

def manage_test_marks(request):
    return render(request, 'class_tests/manage_test_marks.html')

def test_result(request):
    return render(request, 'class_tests/test_result.html')
def class_test_results(request):
    # UI only for now
    return render(request, "class_tests/test_results.html")

# def login_view(request):
#     # if already logged in, go to dashboard

#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         try:
#             response = requests.post(
#                 f"{FASTAPI_BASE_URL}/auth/login",
#                 json={"email": email, "password": password},
#                 timeout=10
#             )

#             if response.status_code == 200:
#                 data = response.json()
#                 request.session["access_token"] = data["access_token"]
#                 request.session["user"] = data["user"]

#                 return redirect("core:dashboard")

#             return render(request, "base/login.html", {"error": "Invalid credentials"})

#         except requests.exceptions.RequestException:
#             return render(request, "base/login.html", {"error": "Backend not reachable"})

#     return render(request, "base/login.html")


def logout_view(request):
    request.session.flush()
    return redirect("core:login")

# @login_required
# def login_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if not request.session.get("access_token"):
#             return redirect("core:login")
#         return view_func(request, *args, **kwargs)
#     return wrapper
def promotion_history(request):
    return render(request, "students/promotion_history.html")

def view_syllabus(request):
    return render(request, "syllabus/view_syllabus.html")
def timetable_weekdays(request):
    return render(request, "timetable/weekdays.html")
def timetable_periods(request):
    return render(request, "timetable/periods.html")
def timetable_class(request):
    return render(request, "timetable/class_timetable.html")
def timetable_print(request):
    return render(request, "timetable/timetable_print.html")
def timetable_teacher(request):
    return render(request, "timetable/teacher_timetable.html")
def employees_attendance_sheet(request):
    if not request.session.get("auth"):
        return redirect("core:login")

    try:
        response = api_request(request, "GET", "/employees")
        employees = response.json()
    except PermissionError:
        return redirect("core:login")

    return render(
        request,
        "attendance/employees_attendance_sheet.html",
        {"employees": employees}
    )


def students_attendance_search(request):
    print("SESSION DATA:", request.session.items())
    auth = request.session.get("auth")

    if not auth or "access_token" not in auth:
        return redirect("core:login")  # 🔥 THIS WAS MISSING

    token = auth["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        classes_resp = api_request(request, "GET", "/classes/")
        sections_resp = api_request(request, "GET", "/sections/")
    except PermissionError:
        return redirect("core:login")

    classes = classes_resp.json()
    sections = sections_resp.json()


    return render(
        request,
        "attendance/students_attendance_search.html",
        {
            "classes": classes,
            "sections": sections
        }
    )

def students_attendance_sheet(request):
    if not request.session.get("auth"):
        return redirect("core:login")

    date = request.GET.get("date")
    class_id = request.GET.get("class_id")
    section_id = request.GET.get("section_id")

    params = {}
    if section_id:
        params["section_id"] = section_id

    try:
        response = api_request(
            request,
            "GET",
            f"/students/by-class/{class_id}",
            params=params
        )
        students = response.json()
    except PermissionError:
        return redirect("core:login")

    return render(
        request,
        "attendance/students_attendance_sheet.html",
        {
            "students": students,
            "date": date,
            "class_id": class_id,
            "section_id": section_id,
        }
    )
def students_attendance_report(request):
    token = request.session.get("auth", {}).get("access_token")

    if not token:
        return redirect("core:login")

    # Default date range = this month
    from datetime import date
    today = date.today()
    start_date = request.GET.get("start_date", today.replace(day=1).isoformat())
    end_date = request.GET.get("end_date", today.isoformat())

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = api_request(
            request,
            "GET",
            "/attendance-reports/students",
            params={
            "start_date": start_date,
            "end_date": end_date
            }
        )
        records = response.json()
    except PermissionError:
        return redirect("core:login")


    records = response.json() if response.status_code == 200 else []

    return render(
        request,
        "attendance/students_attendance_report.html",
        {
            "records": records,
            "start_date": start_date,
            "end_date": end_date
        }
    )
def employees_attendance_report(request):
    if not request.session.get("auth"):
        return redirect("core:login")

    from datetime import date
    today = date.today()

    start_date = request.GET.get("start_date", today.replace(day=1).isoformat())
    end_date = request.GET.get("end_date", today.isoformat())
    search = request.GET.get("search", "").strip()

    try:
        response = api_request(
            request,
            "GET",
            "/attendance-reports/employees",
            params={"start_date": start_date, "end_date": end_date}
        )
        records = response.json()
    except PermissionError:
        return redirect("core:login")

    if search:
        records = [
            r for r in records
            if search.lower() in r["employee_name"].lower()
        ]

    return render(
        request,
        "attendance/employees_attendance_report.html",
        {
            "records": records,
            "start_date": start_date,
            "end_date": end_date,
            "search": search,
        }
    )
def class_wise_report(request):
    from datetime import date

    auth = request.session.get("auth")
    if not auth:
        return redirect("core:login")

    token = auth["access_token"]

    date_value = request.GET.get("date", date.today().isoformat())
    class_name = request.GET.get("class_name", "10")
    section = request.GET.get("section", "")

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        "https://erp.backend.smartbus360.com/attendance-reports/students/class-wise",
        headers=headers,
        params={
            "class_name": class_name,
            "section": section or None,
            "date_value": date_value
        }
    )

    records = response.json() if response.status_code == 200 else []

    present = sum(1 for r in records if r["status"] == "present")
    absent = sum(1 for r in records if r["status"] == "absent")
    leave = sum(1 for r in records if r["status"] == "leave")
    total = present + absent + leave

    return render(request, "attendance/class_wise_report.html", {
        "records": records,
        "date_value": date_value,
        "class_name": class_name,
        "section": section,
        "present": present,
        "absent": absent,
        "leave": leave,
        "total": total,
    })

# core/views/exams.py
# def get_auth_header(request):
#     auth = request.session.get("auth")
#     if not auth:
#         return {}

#     return {
#         "Authorization": f"Bearer {auth.get('access_token')}"
#     }
def exam_schedule(request, exam_id):
    return render(
        request,
        "exams/exam_schedule.html",
        {
            "exam_id": exam_id
        }
    )
def create_exam(request):
    return render(request, "exams/create_exam.html")
def fee_fine_settings(request):
    return render(request, "fees/fee_fine_settings.html")
# def salary_slip_view(request, payment_id):
#     auth = request.session.get("auth")

#     if not auth:
#         return redirect("core:login")

#     token = auth["access_token"]

#     response = requests.get(
#         f"{FASTAPI_BASE_URL}/salary/slip/{payment_id}",
#         headers={
#             "Authorization": f"Bearer {token}"
#         }
#     )

#     if response.status_code != 200:
#         return redirect("core:pay_salary")

#     slip = response.json()

#     return render(
#         request,
#         "salary/salary_paid_slip.html",
#         {
#             "slip": slip
#         }
#     )

def salary_slip_page(request):
    auth = request.session.get("auth")

    # 🔐 Session check
    if not auth or "access_token" not in auth:
        return redirect("core:login")

    payment_id = request.GET.get("payment_id")
    if not payment_id:
        return redirect("core:pay_salary")

    try:
        response = api_request(
            request,
            "GET",
            f"/salary/slip/{payment_id}"
        )
    except PermissionError:
        return redirect("core:login")

    # 🔴 IMPORTANT: check status BEFORE parsing JSON
    if response.status_code != 200:
        print("FASTAPI STATUS:", response.status_code)
        print("FASTAPI BODY:", response.text)
        return redirect("core:pay_salary")

    # ✅ Parse JSON only once, safely
    try:
        slip = response.json()
    except ValueError:
        print("INVALID JSON:", response.text)
        return redirect("core:pay_salary")

    return render(
        request,
        "salary/salary_paid_slip.html",
        {"slip": slip}
    )

def messaging_home(request):
    return render(request, "messaging/messaging.html")


def messages_inbox(request):
    return render(request, "messaging/inbox.html")


def messages_compose(request):
    return render(request, "messaging/compose.html")


def view_message(request, message_id):
    return render(request, "messaging/view_message.html", {
        "message_id": message_id
    })
