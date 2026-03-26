from pathlib import Path

needs_action = Path("Needs_Action")
done = Path("Done")
plans = Path("Plans")

print("Processor start ho gaya...")

for file in needs_action.glob("*.txt"):
    content = file.read_text()

    # 🔥 Priority check
    if "urgent" in content.lower():
        priority = "HIGH"
    else:
        priority = "NORMAL"

    # 🎯 Action detect
    if "invoice" in content.lower():
        action = "Generate invoice"
    else:
        action = "General task"

    # 🧠 Smart plan
    plan = f"""
# Plan for {file.name}

## Task:
{content}

## Priority:
{priority}

## Action:
{action}

## Suggested Reply:
"Thank you for your message. I will handle this task soon."

## Steps:
- Read task
- Prepare response
- Complete task
"""

    # 📄 Plan file create
    plan_file = plans / f"PLAN_{file.stem}.md"
    plan_file.write_text(plan)

    # 🔐 Approval file banana
    approval_folder = Path("approval_pending")
    approval_file = approval_folder / f"APPROVAL_{file.stem}.md"

    approval_content = f"""
# Approval Required

Task: {file.name}

Content:
{content}

Action: {action}

  Move this file to 'approval_done' folder to approve
"""

    approval_file.write_text(approval_content)

    print(f"{file.name} approval ke liye bhej diya gaya")

    # ✅ Approved files process karna
approved_folder = Path("approval_done")

for file in approved_folder.glob("*.md"):
    task_name = file.stem.replace("APPROVAL_", "") + ".txt"
    
    original_file = needs_action / task_name
    
    if original_file.exists():
        content = original_file.read_text()
        
        done_file = done / task_name
        done_file.write_text(content)
        
        original_file.unlink()
    
    file.unlink()
    
    print(f"{task_name} approved aur complete ho gaya")