import datetime , time

def print_with_timestamp(*messages):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, messages))
    print(f"[{timestamp}] {message}")

def print_input_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", end="")