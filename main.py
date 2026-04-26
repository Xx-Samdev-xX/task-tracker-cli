from argparse import ArgumentParser
import json
from datetime import datetime
from time import sleep

path = "Tasks.json"

def open_json():
    with open(path,"r") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open(path,"w") as f:
        json.dump(data, f, indent= 4)

def print_task(data, index):
    print(f"""Task:\nNumber: {data[index]["id"]}
Name: {data[index]["name"]}
Description:{data[index]["description"]}
Status: {data[index]["status"]}
Created:{data[index]["createdAt"]}
Updated: {data[index]["updatedAt"]}""")
    print()
    
def listing(status, data):
    print(f"List of tasks with '{status}' status")
    found = False
    for task in range(len(data)):
        if data[task]["status"] == status:
            found = True
            print_task(data, task)
            print()
    if not found:
        sleep(1)
        print(f"No tasks with '{status}' status found")
def now_time():
    now = datetime.now()
    now = now.strftime("%d/%m/%Y, %H:%M:%S")
    return now
def add_fn(args):
    data = open_json()
    new_id = len(data) + 1
    now = now_time()
    data.append({
        "id": new_id,
        "name": args.name,
        "description": args.desc,
        "status": "to-do",
        "createdAt": now,
        "updatedAt": now})
    
    save_json(data)
    print_task(data, -1)
    print(f"Added: Name: {args.name}. Desc: {args.desc}")

def update_fn(args):
    data = open_json()
    data[args.id-1]["name"] = args.name
    data[args.id-1]["description"] = args.desc
    now=now_time()
    data[args.id-1]["updatedAt"] = now
    save_json(data)
    print("Updated task")
    sleep(0.5)
    print_task(data, args.id -1)
    print(f"Update task id:{args.id}, name:{args.name}, desc:{args.desc}")

def delete_fn(args):
    data = open_json()

    data.pop(args.id-1)

    for task in range(len(data)):
            data[task]["id"] = task + 1 #updating id to match since if we delete in the midle id's will be messed up!
    save_json(data)
    print("Delted successfully")
    
def mark_fn(args):
    data = open_json()
    data[args.id -1 ]["status"] = args.status
    now = now_time()

    data[args.id - 1]["updatedAt"] = now
    save_json(data)
    print("Updated task..")
    print_task(data, args.id -1)
    print(f"Task id: {args.id} new-status: {args.status}")

def list_fn(args):
    if args.todo:
        data = open_json()
        listing("to-do", data)
        print()
        print("Listed task with to-do status")
    elif args.done:
        data = open_json()
        listing("done", data)
        print()
        print("Listed task with done status")
    elif args.inprogress:
        data = open_json()
        listing("in-progress" ,data)
        print()
        print("Listed task with in-progress status")
    else:
        data = open_json()
        print("List of all tasks.")
        sleep(0.5)
        [print_task(data, task) for task in range(len(data)) ]
        print("Listed all tasks")

def status_count(status, data):
    count = 0
    for val in range(len(data)):
        if data[val]["status"] == status:
            count += 1
    return count
def stats_fn():
    data = open_json()
    total_num = len(data)
    to_do = status_count("to-do", data)
    done = status_count("done", data)
    in_progress = status_count("in-progress", data)
    print(f"Status\nTotal tasks: {total_num}\nTo-do tasks: {to_do}\nDone tasks: {done}\nIn-progress Tasks: {in_progress}")

parser = ArgumentParser()
subparser = parser.add_subparsers(dest="command")

add = subparser.add_parser("add")
add.add_argument("name", help="Name of the task")
add.add_argument("--desc", help="Enter new despription", default="None")
add.set_defaults(func = add_fn)

update_cmd = subparser.add_parser("update")
update_cmd.add_argument("id", help="Id of the task to update", type= int)
update_cmd.add_argument("name", help="New name of the task")
update_cmd.add_argument("--desc", help="Description of the task", default="None")
update_cmd.set_defaults(func = update_fn)

delete_cmd = subparser.add_parser("delete")
delete_cmd.add_argument("id", help = "Id of the task to delete", type=int)
delete_cmd.set_defaults(func = delete_fn)

mark_cmd = subparser.add_parser("mark")
mark_cmd.add_argument("id", help="Id of task to change status", type=int)
mark_cmd.add_argument("status", choices=["to-do", "done", "in-progress"], help="Choose status of the new task")
mark_cmd.set_defaults(func = mark_fn)

list_cmd = subparser.add_parser("list")
list_cmd.add_argument("--todo", help="List to do status", action="store_true")
list_cmd.add_argument("--done", help="List done status", action="store_true")
list_cmd.add_argument("-inp", "--inprogress", help="List inprogress status", action="store_true")
list_cmd.set_defaults(func = list_fn)

stats_cmd = subparser.add_parser("stats")
stats_cmd.set_defaults(func = stats_fn)

args= parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()

