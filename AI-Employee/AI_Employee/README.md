# 🤖 Personal AI Employee (Hackathon Project)

## 🚀 Overview

This project is a **Personal AI Employee (Digital FTE)** built as part of the hackathon.
It simulates a smart assistant that can automatically:

* 📥 Detect tasks
* 🧠 Create plans
* ⏳ Ask for approval
* ✅ Complete tasks
* 📊 Update dashboard

The system works using a **local-first approach** with simple Python automation.

---

## 🎯 Features

### 🟢 1. Watcher (Perception Layer)

* Monitors the `Inbox` folder
* Moves new files to `Needs_Action`

### 🟢 2. Processor (Reasoning Layer)

* Reads tasks from `Needs_Action`
* Detects priority (Normal / High)
* Generates a plan file in `Plans`

### 🟢 3. Approval System (Human-in-the-Loop)

* Creates approval files in `approval_pending`
* User manually approves by moving files to `approval_done`

### 🟢 4. Task Completion

* After approval, tasks move to `Done`
* Dashboard updates automatically

### 🟢 5. CEO Report (Gold Feature)

* Tracks completed tasks
* Provides simple business insights

---

## 🗂 Folder Structure

```
AI-Employee/
│
├── Inbox/
├── Needs_Action/
├── Plans/
├── Done/
├── approval_pending/
├── approval_done/
│
├── watcher.py
├── processor.py
├── run_all.py
├── Dashboard.md
├── Business_Goals.md
├── CEO_Report.md
└── README.md
```

---

## ⚙️ How It Works (Simple Flow)

1. Create a task in `Inbox`
2. Run watcher:

```
python watcher.py
```

➡ moves task to `Needs_Action`

3. Run processor:

```
python processor.py
```

➡ creates plan + approval file

4. Approve task:
   ➡ move file from `approval_pending` → `approval_done`

5. Run processor again:

```
python processor.py
```

➡ task completed and moved to `Done`

---

## 🧪 Example Task

**Input:**

```
client ne invoice urgent manga he
```

**Output:**

* Plan generated
* Priority = HIGH
* Approval required
* Task completed after approval

---

## 🏆 Hackathon Tier

✅ Bronze Tier – Completed
✅ Silver Tier – Completed
✅ Gold Tier – Basic Implementation Completed

---

## 🔐 Security

* No real APIs used (safe for testing)
* Manual approval required before actions
* Local file-based system (no cloud risk)

---

## 💡 Future Improvements

* Gmail & WhatsApp integration
* Automatic email replies
* Real CEO business analytics
* MCP server integration

---

## 👩‍💻 Author

**Name:** Erum Abbas
**Institute:** GIAIC
**Class:** Sunday Afternoon
**Teacher:** Sir Ali Jawwad

---

## 🎉 Final Note

This project demonstrates how an AI can act like a **digital employee**, helping automate daily tasks with minimal human effort.

---

⭐ If you like this project, feel free to star the repo!
