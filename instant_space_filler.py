import os

import psutil

chosen_drive = ()

def disk_choose():
    global chosen_drive

    disks = psutil.disk_partitions()
    print("Добро пожаловать в заполнитель места от Romeo558! Выберите диск, который вы хотите уничтожить:")
    print("Доступные диски:")
    for i, disk in enumerate(disks):
        print(f"{i + 1}. {disk.device}")

    disk_num = int(input("Выберите диск (введите номер): "))
    selected_disk = disks[disk_num - 1]

    disk_usage = psutil.disk_usage(selected_disk.mountpoint)

    usage_b = disk_usage.free
    usage_kb = disk_usage.free / 1024
    usage_mb = disk_usage.free / (1024 * 1024)
    usage_gb = disk_usage.free / (1024 * 1024 * 1024)
    chosen_drive = selected_disk

    print(f"\nДоступное место на диске {selected_disk.device}:")
    print(f"В байтах: {usage_b} байт")
    print(f"В килобайтах: {usage_kb} КБ")
    print(f"В мегабайтах: {usage_mb} МБ")
    print(f"В гигабайтах: {usage_gb} ГБ")
    return [usage_b, usage_kb, usage_mb, usage_gb, chosen_drive]


def spacefiller(usage: list):
    global chosen_drive
    usage_b = usage[0]
    spacefiller_command = f"fsutil file createnew {str(chosen_drive[1])}go_touch_some_grass.for_real {int(usage_b).real}"
    return spacefiller_command


spaceKILLER = spacefiller(disk_choose())
print(spaceKILLER)
os.system(spaceKILLER)
