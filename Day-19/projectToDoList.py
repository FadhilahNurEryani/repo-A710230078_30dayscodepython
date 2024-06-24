class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("Tidak ada tugas.")
        else:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

        
    def mark_done(self, task_number):
        if 0 <= task_number - 1 < len(self.tasks):
            self.tasks[task_number - 1] = f"{self.tasks[task_number - 1]} (Selesai)"
        else:
            print("Nomer tugas tidak valid.")

def main():
    my_list = ToDoList()
    while True:
        print("\n===== To-Do List =====")
        print("1. Tambahkan tugas")
        print("2. Lihat tugas")
        print("3. Tandai tugas selesai")
        choice = input("Masukkan pilihan anda: ")

        if choice == '1':
            print()
            task = input("Masukkan pilihan anda: ")
            my_list.add_task(task)
            print("Tugas ditambahkan!")

        elif choice == '2':
            my_list.view_tasks()

        elif choice == '3':
            task_number = int(input("Masukkan tugas yang telah diselesaikan: "))
            my_list.mark_done(task_number)

        else:
            print("Masukkan piliham yang valid.")

if __name__ == "__main__":
    main()