from collections import deque, defaultdict

class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packets = deque()
        self.packet_set = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        if len(self.packets) >= self.memory_limit:
            oldest_packet = self.packets.popleft()
            self.packet_set.remove(oldest_packet)
        self.packets.append(packet)
        self.packet_set.add(packet)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.packets:
            return []
        packet = self.packets.popleft()
        self.packet_set.remove(packet)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        count = 0
        for _, dest, timestamp in self.packets:
            if dest == destination and startTime <= timestamp <= endTime:
                count += 1
        return count

def solve(*args, **kwargs):
    # This function is a placeholder to demonstrate the entry point.
    # In practice, it would handle input parsing and method invocation.
    pass