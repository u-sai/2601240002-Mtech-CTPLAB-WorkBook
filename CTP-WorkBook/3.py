from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


@dataclass
class Queue(Generic[T]):
    items: list[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


stack = Stack[int]()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Popped:", stack.pop())
print("Top:", stack.peek())


queue = Queue[str]()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Queue:", queue.items)
print("Dequeued:", queue.dequeue())
print("Front:", queue.front())
