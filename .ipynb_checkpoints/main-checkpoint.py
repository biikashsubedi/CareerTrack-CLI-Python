import csv
from datetime import datetime

CSV_FILE = "jobs.csv"

# SET UP THE FILE READER
def load_applications():
    # Reads all job applications
    applications = []
    try:
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                applications.append(row)
    except FileNotFoundError:
        return []
    return applications


# THE REMINDER ENGINE & DISPLAY
def check_reminders(applications):
    # Filters applications for follow-ups and upcoming deadlines.
    today = datetime.now().date()
    
    print("DAILY JOB TRACKER REMINDERS")
    print("="*40)
    
    reminders_found = False
    
    for app in applications:
        # active applications
        if app['Status'] in ['Applied', 'Interviewing']:
            try:
                follow_up_date = datetime.strptime(app['Follow-up Date'], "%Y-%m-%d").date()
                deadline_date = datetime.strptime(app['Deadline'], "%Y-%m-%d").date()
                
                if today >= follow_up_date:
                    print(f"FOLLOW-UP It's time to reach out to {app['Company']} for the '{app['Job Title']}' role!")
                    print(f"(Scheduled for: {app['Follow-up Date']} | Current Status: {app['Status']})\n")
                    reminders_found = True
                    
                days_to_deadline = (deadline_date - today).days
                if 0 <= days_to_deadline <= 3:
                    print(f"URGENT DEADLIN '{app['Job Title']}' at {app['Company']} is due in {days_to_deadline} days! ({app['Deadline']})\n")
                    reminders_found = True
                    
            except ValueError:
                print(f"Error parsing dates for {app['Company']}. Ensure format is YYYY-MM-DD.")

    if not reminders_found:
        print("No pending follow-ups or urgent deadlines today.")


# USER INTERACTION, ADD NEW JOBS
def add_application():
    # new application to the CSV file
    print("\n--- Add New Job Application ---")
    title = input("Job Title: ")
    company = input("Company Name: ")
    app_date = input("Application Date (YYYY-MM-DD) [Leave blank for today]: ")
    
    if not app_date:
        app_date = datetime.now().strftime("%Y-%m-%d")
        
    status = input("Status (Applied/Interviewing/Rejected/Offer) [Default: Applied]: ")
    if not status:
        status = "Applied"
        
    deadline = input("Application/Interview Deadline (YYYY-MM-DD): ")
    follow_up = input("Follow-up Date (YYYY-MM-DD): ")
    notes = input("Notes: ")

    fieldnames = ['Job Title', 'Company', 'Application Date', 'Status', 'Deadline', 'Follow-up Date', 'Notes']
    
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header only if the file is completely empty
        if file.tell() == 0:
            writer.writeheader()
            
        writer.writerow({
            'Job Title': title,
            'Company': company,
            'Application Date': app_date,
            'Status': status,
            'Deadline': deadline,
            'Follow-up Date': follow_up,
            'Notes': notes
        })
    print(f"Successfully added '{title}' at {company} to your tracker!")


def main():
    while True:
        print("=== JOB APPLICATION TRACKER MENU ===")
        print("1. Check Reminders & Dashboard")
        print("2. Add a New Job Application")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            apps = load_applications()
            if not apps:
                print("\nYour tracker is currently empty. Try adding a job first!\n")
            else:
                check_reminders(apps)
        elif choice == '2':
            add_application()
        elif choice == '3':
            print("\nGoodbye! Good luck with your job hunt! 👋")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()