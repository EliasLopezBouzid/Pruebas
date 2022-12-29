import argparse
import datetime

def add(args):
    if args.priority == None:
        args.priority = 'Normal'
    task = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")};{args.priority};{args.name}'
    with open('task.csv', 'a') as f:
        f.write(task + "\n")
        
def list(args):
    with open('task.csv', 'r') as f:
        data = f.readlines()
        for line in data:
            if args.priority == None:
                print(line)
            else:
                if args.priority in line:
                    print(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, help='Especifique accion')
    parser.add_argument('--name', type=str, help='Especifique nombre de tarea')
    parser.add_argument('--priority',
                        type=str,
                        choices=['Low', 'Normal', 'High'],
                        help='Especifique prioridad(Low,Normal,High)'
                        )
    args = parser.parse_args()
    if args.action == "add":
        add(args)
    if args.action == "list":
        list(args)
    
if __name__ == '__main__':
    main()