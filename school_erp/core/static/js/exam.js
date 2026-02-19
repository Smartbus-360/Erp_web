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
        "Authorization":"Bearer " + window.ACCESS_TOKEN,
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
