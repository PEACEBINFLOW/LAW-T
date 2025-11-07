import sys
from lawt.cli import cmd_law_add, cmd_ledger_list

def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv or argv[0] in ('-h','--help'):
        print('Usage: python src/main.py [law add <path>] | [ledger list]')
        return 0
    if argv[0] == 'law' and len(argv) >= 3 and argv[1] == 'add':
        return cmd_law_add(argv[2])
    if argv[0] == 'ledger' and len(argv) >= 2 and argv[1] == 'list':
        return cmd_ledger_list()
    print('Unknown command')
    return 1

if __name__ == '__main__':
    raise SystemExit(main())
