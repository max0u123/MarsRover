import datetime

def print_with_timestamp(*messages):
    """
    Imprime un message avec un horodatage au format HH:MM:SS.

    Args:
        *messages: Les messages à imprimer (peut être plusieurs arguments).

    Example:
        print_with_timestamp("Message 1", "Message 2")
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, messages))
    print(f"[{timestamp}] {message}")

def print_input_with_timestamp(message):
    """
    Imprime un message avec un horodatage au format HH:MM:SS, sans saut de ligne à la fin.

    Args:
        message (str): Le message à imprimer.

    Example:
        print_input_with_timestamp("Message d'entrée")
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", end="")