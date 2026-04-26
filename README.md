# Task Tracker CLI

A powerful and beginner-friendly **Command Line Task Manager** built with Python.
This tool allows you to manage your daily tasks efficiently from your terminal — with clean structure, persistent storage, and a smooth developer-style interface.

##  Overview

**Task Tracker CLI** is a lightweight productivity tool that lets you:

* Add new tasks
* View all tasks or filter by status
* Update task details
* Delete tasks
* Change task status (to-do, in-progress, done)
* View task statistics

All tasks are stored locally using a JSON file, making the tool simple, fast, and easy to extend.

##Requirements

**  Python 3 (obviously )

## Usage

## Commands

### Add a Task

```bash
python main.py add "Learn Python" --desc "Practice CLI projects"
```
** --desc is optional **

### 📋 List Tasks

List all tasks:

```bash
python main.py list
```
Filter by status:

```bash
python main.py list --todo
python main.py list --done
python main.py list --inprogress
```
---

### Update a Task

```bash
python main.py update 1 "New Task Name" --desc "Updated description"
```
python main.py update (task id) "New Task Name" --desc "Updated description" (optional description)
### Delete a Task

```bash
python main.py delete 1
```
python main.py delete (task id)

### Change Task Status

```bash
python main.py mark 1 done
python main.py mark 1 in-progress
python main.py mark 1 to-do
```
python main.py mark (task id) (New status)
---

### View Statistics

```bash
python main.py stats
```

Displays:

* Total tasks
* To-do tasks
* Completed tasks
* Tasks in progress

---

## Task Format

Each task is stored as:

```json
{
  "id": 1,
  "name": "Learn Python",
  "description": "Practice CLI projects",
  "status": "to-do",
  "createdAt": "26/04/2026, 10:30:00",
  "updatedAt": "26/04/2026, 10:30:00"
}
```
##  Features

*  Clean CLI command structure using subparsers
*  Simple and intuitive commands
*  Persistent storage using JSON
*  Built-in statistics tracking
*  Auto-updating timestamps
*  Beginner-friendly but scalable design
---

## Notes

* Task IDs are reassigned after deletion to maintain order
* `tasks.json` is created automatically if it doesn’t exist
* Designed for local usage (not multi-user)
---

##  Future Improvements

* Due dates and reminders
* Task priorities
* Search functionality
* Web version using FastAPI
* Packaging as a global CLI tool

## Author

Built by **Samuel** as part of a journey into Python, backend development, and AI.

## License
This project is open-source and free to use.

## Credits
https://roadmap.sh/projects/task-tracker
