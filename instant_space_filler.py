"""
Instant Space Filler (ISF)

A utility for creating files of specific sizes to test storage limits.
"""

import os
import argparse
import psutil
import ctypes
import sys

def is_admin():
    """Check if running with administrator privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def list_disks():
    """Display available storage devices"""
    disks = psutil.disk_partitions()
    print("Available storage devices:")
    for idx, disk in enumerate(disks):
        usage = psutil.disk_usage(disk.mountpoint)
        print(f"{idx + 1}. {disk.device} ({usage.free / (1024**3):.2f} GB free)")

def create_file(path, size_bytes):
    """Create file of specified size using fsutil"""
    try:
        os.system(f'fsutil file createnew "{path}" {size_bytes}')
        print(f"Successfully created {size_bytes} byte file at {path}")
    except Exception as e:
        print(f"Error creating file: {str(e)}")

def auto_fill(drive_letter, file_name="space_filler.dat"):
    """Automatically fill a drive to capacity"""
    drive_path = f"{drive_letter}:\\{file_name}"
    try:
        usage = psutil.disk_usage(f"{drive_letter}:\\")
        create_file(drive_path, usage.free)
    except Exception as e:
        print(f"Error filling drive: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="Instant Space Filler - Storage allocation utility",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command')

    # Auto-fill command
    fill_parser = subparsers.add_parser('fill', help='Automatically fill a drive')
    fill_parser.add_argument('-d', '--drive', required=True, 
                           help='Drive letter to fill (e.g., C)')
    fill_parser.add_argument('-n', '--name', default='space_filler.dat',
                           help='Filename to create (default: space_filler.dat)')

    # Manual create command
    create_parser = subparsers.add_parser('create', help='Create custom file')
    create_parser.add_argument('-p', '--path', required=True,
                             help='Full file path including filename')
    create_parser.add_argument('-s', '--size', required=True,
                             help='File size (supports KB, MB, GB suffixes)\n'
                                  'Example: 10GB, 500MB, 1024KB')

    # List command
    list_parser = subparsers.add_parser('list', help='Show available storage devices')

    args = parser.parse_args()

    if args.command == 'list':
        list_disks()
    elif args.command == 'fill':
        if args.drive.upper() == 'C' and not is_admin():
            print("Administrator privileges required for system drive!")
            sys.exit(1)
            
        auto_fill(args.drive.upper(), args.name)
    elif args.command == 'create':
        # Convert size to bytes
        size = args.size.upper()
        try:
            if size.endswith('GB'):
                bytes_size = int(float(size[:-2]) * (1024**3)
            elif size.endswith('MB'):
                bytes_size = int(float(size[:-2]) * (1024**2)
            elif size.endswith('KB'):
                bytes_size = int(float(size[:-2]) * 1024
            else:
                bytes_size = int(size)
        except ValueError:
            print("Invalid size format! Use numbers with optional KB/MB/GB suffix")
            sys.exit(1)
            
        create_file(args.path, bytes_size)
    else:
        parser.print_help()

if __name__ == "__main__":
    if not sys.platform.startswith('win'):
        print("This utility requires Windows OS")
        sys.exit(1)
        
    main()
