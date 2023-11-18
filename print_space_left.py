import psutil


def get_disk_info():
    disks = psutil.disk_partitions()
    print("Доступные диски:")
    for i, disk in enumerate(disks):
        print(f"{i + 1}. {disk.device}")

    disk_num = int(input("Выберите диск (введите номер): "))
    selected_disk = disks[disk_num - 1]

    disk_usage = psutil.disk_usage(selected_disk.mountpoint)
    print(f"\nДоступное место на диске {selected_disk.device}:")
    print(f"{disk_usage.free} байт")


get_disk_info()