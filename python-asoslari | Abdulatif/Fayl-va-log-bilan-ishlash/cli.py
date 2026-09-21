import argparse

parser = argparse.ArgumentParser(description="Service Manager")

subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("start", help="Start the service")
subparsers.add_parser("stop", help="Stop the service")

args = parser.parse_args()

if args.command == "start":
    print("Service started")

elif args.command == "stop":
    print("Service stopped")

else:
    parser.print_help()
