document.addEventListener("DOMContentLoaded", () => {

  const form = document.getElementById("createExamForm");
  if (!form) return;


  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fd = new FormData(form);

    const payload = {
      name: fd.get("name"),
      class_id: Number(fd.get("class_id")),
      start_date: fd.get("start_date"),
      end_date: fd.get("end_date"),
      subject_ids: [...document.querySelectorAll("input[name='subject_ids']:checked")]
        .map(i => Number(i.value))
    };

    const res = await fetch("https://erp.backend.smartbus360.com/exams/", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + window.ACCESS_,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      alert("Failed to create exam");
      return;
    }

    const exam = await res.json();

    // 👉 redirect to schedule page
    window.location.href = `/exams/${exam.id}/schedule/`;
  });
});

async function saveSchedule(examId, classId, sectionId) {

  const rows = document.querySelectorAll("tbody tr");
  const schedules = [];

  rows.forEach(row => {
    const subjectId = row.dataset.subject;
    if (!subjectId) return;

    const date = row.querySelector(".exam-date")?.value;
    const teacher = row.querySelector(".teacher-select")?.value;

    if (date && teacher) {
      schedules.push({
        exam_date: date,
        subject_id: Number(subjectId),
        teacher_id: Number(teacher)
      });
    }
  });

  if (!schedules.length) {
    alert("Please assign at least one subject date");
    return;
  }

  const res = await fetch(
    `https://erp.backend.smartbus360.com/exams/${examId}/schedule`,
    {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + window.ACCESS_TOKEN,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        class_id: classId,
        section_id: sectionId,
        schedules
      })
    }
  );

  alert(res.ok ? "Schedule saved" : "Error saving schedule");
}
