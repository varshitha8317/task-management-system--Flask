const BASE_URL = "http://127.0.0.1:5000/api/v1";

/* ================= LOGIN ================= */

function login() {
    fetch(BASE_URL + "/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            document.getElementById("loginSection").classList.add("hidden");
            document.getElementById("dashboardSection").classList.remove("hidden");
        } else {
            alert("Login failed");
        }
    });
}

function logout() {
    localStorage.removeItem("token");
    location.reload();
}

function getToken() {
    return localStorage.getItem("token");
}

/* ================= HOME ================= */

function showHome() {
    document.getElementById("contentArea").innerHTML = `
        <h2>Welcome 👋</h2>
        <p>Select an option from sidebar.</p>
    `;
}

/* ================= PROJECTS ================= */

function showProjects() {
    document.getElementById("contentArea").innerHTML = `
        <h3>Create Project</h3>
        <div id="projectMessage"></div>

        <input type="text" id="projectName" class="form-control mb-2" placeholder="Project Name">
        <button class="btn btn-success mb-2" onclick="createProject()">Create</button>
        <button class="btn btn-primary mb-3" onclick="loadProjects()">View Projects</button>

        <div id="projectList"></div>
    `;
}

function createProject() {
    fetch(BASE_URL + "/projects/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify({
            name: document.getElementById("projectName").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("projectMessage").innerHTML =
            `<div class="alert alert-success">Project created successfully!</div>`;
        document.getElementById("projectName").value = "";
    });
}

function loadProjects() {
    fetch(BASE_URL + "/projects/", {
        headers: { "Authorization": "Bearer " + getToken() }
    })
    .then(res => res.json())
    .then(data => {
        let html = "<ul class='list-group'>";
        data.forEach(p => {
            html += `<li class="list-group-item">ID: ${p.id} - ${p.name}</li>`;
        });
        html += "</ul>";
        document.getElementById("projectList").innerHTML = html;
    });
}

/* ================= TASKS ================= */

function showTasks() {
    document.getElementById("contentArea").innerHTML = `
        <h3>Create Task</h3>
        <div id="taskMessage"></div>

        <input type="text" id="taskTitle" class="form-control mb-2" placeholder="Title">
        <input type="text" id="taskDescription" class="form-control mb-2" placeholder="Description">
        <input type="text" id="taskPriority" class="form-control mb-2" placeholder="low / medium / high">
        <input type="number" id="taskProjectId" class="form-control mb-2" placeholder="Project ID">
        <input type="number" id="taskUserId" class="form-control mb-2" placeholder="Employee ID">

        <button class="btn btn-warning mb-2" onclick="createTask()">Create Task</button>
        <button class="btn btn-primary mb-3" onclick="loadTasks()">View Tasks</button>

        <div id="taskList"></div>
    `;
}

function createTask() {
    fetch(BASE_URL + "/tasks/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify({
            title: document.getElementById("taskTitle").value,
            description: document.getElementById("taskDescription").value,
            priority: document.getElementById("taskPriority").value,
            project_id: parseInt(document.getElementById("taskProjectId").value),
            assigned_user_ids: [
                parseInt(document.getElementById("taskUserId").value)
            ]
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("taskMessage").innerHTML =
            `<div class="alert alert-success">Task created successfully!</div>`;
    });
}

function loadTasks() {
    fetch(BASE_URL + "/tasks/", {
        headers: { "Authorization": "Bearer " + getToken() }
    })
    .then(res => res.json())
    .then(data => {
        let html = "<ul class='list-group'>";
        data.forEach(t => {
            html += `<li class="list-group-item">
                        ID: ${t.id} | ${t.title} | ${t.priority} | ${t.status}
                     </li>`;
        });
        html += "</ul>";
        document.getElementById("taskList").innerHTML = html;
    });
}

/* ================= ANALYTICS ================= */

function loadAnalytics() {
    fetch(BASE_URL + "/analytics/status", {
        headers: { "Authorization": "Bearer " + getToken() }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("contentArea").innerHTML = `
            <h3>Analytics</h3>
            <div class="row mt-4">
                <div class="col-md-4">
                    <div class="dashboard-card bg-primary">
                        <h5>Total Tasks</h5>
                        <h2>${data.total_tasks}</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="dashboard-card bg-success">
                        <h5>Completed</h5>
                        <h2>${data.completed_tasks}</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="dashboard-card bg-danger">
                        <h5>Overdue</h5>
                        <h2>${data.overdue_tasks}</h2>
                    </div>
                </div>
            </div>
        `;
    });
}
