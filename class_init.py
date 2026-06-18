class Vehicle:
    running = False

    def __init__(self, owner) -> None:
        self.owner = owner

    def is_running(self):
        if self.running:
            print(f"{self.owner}'s vehicle car is running")

        else:
            print("{self.owner}'s vehicle is not running")

v1 = Vehicle(owner="Ibk")

print(v1.owner)
print(v1.running)
print(v1.is_running())
