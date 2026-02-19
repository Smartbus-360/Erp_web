// =====================
// TOKEN UTILITIES (SESSION BASED)
// =====================


function authHeaders() {
    if (!window.ACCESS_TOKEN) {
        console.warn("No ACCESS_TOKEN found");
        return {};
    }
    return {
        "Authorization": "Bearer " + window.ACCESS_TOKEN,
        "Content-Type": "application/json"
    };
}


// =====================
// CURRENT USER
// =====================
async function getCurrentUser() {
    const token = window.ACCESS_TOKEN;

    if (!token) {
        console.warn("ACCESS_TOKEN missing, skipping auth check");
        return null; // ❗ DO NOT REDIRECT HERE
    }

    const res = await fetch("https://erp.backend.smartbus360.com/auth/me", {
        headers: authHeaders()
    });

    if (!res.ok) {
        console.warn("Auth failed, redirecting to login");
        localStorage.removeItem("access_token");
        window.location.href = "/login/";
        return null;
    }

    return await res.json();
}

