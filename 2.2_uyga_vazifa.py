# 1. Monitoring dictionary

servers = {
    "server1": "up",
    "server2": "down",
    "server3": "up",
    "server4": "down"
}


def show_down_servers(servers):
    for server, status in servers.items():
        if status == "down":
            print(server)


show_down_servers(servers)


# 2. List comprehension

numbers = [x for x in range(1, 51) if x % 3 == 0]

print(numbers)


# 3. Nested function va closure

def outer_function(message):
    def inner_function():
        print(message)

    return inner_function


hello = outer_function("Hello DevOps!")
hello()


# 4. Custom exception

class InvalidServerNameError(Exception):
    pass


def check_server_name(name):
    if not name.startswith("server"):
        raise InvalidServerNameError("Server nomi noto'g'ri!")
    print("Server nomi to'g'ri")


try:
    check_server_name("test")
except InvalidServerNameError as error:
    print(error)


# 5. Port validation

try:
    port = int(input("Port raqamini kiriting: "))

    if port < 1 or port > 65535:
        print("Port noto'g'ri! 1-65535 oralig'ida bo'lishi kerak.")
    else:
        print("Port to'g'ri:", port)

except ValueError:
    print("Xato! Port raqami son bo'lishi kerak.")
