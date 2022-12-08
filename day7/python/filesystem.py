from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import reduce
from typing import Self, Optional


@dataclass
class FilesystemObject(ABC):
    name: str
    parent: Optional[Self]

    @property
    @abstractmethod
    def size(self):
        pass


@dataclass
class File(FilesystemObject):
    file_size: int
    is_directory: bool = False

    @property
    def size(self):
        return self.file_size


@dataclass
class Directory(FilesystemObject):
    children: list[FilesystemObject] = field(default_factory=list)
    is_directory: bool = True

    @property
    def size(self):
        size_sum = 0
        for child in self.children:
            size_sum += child.size
        return size_sum

    def create_child(self, name, size=0, directory=False):
        if any([True for child in self.children if child.name == name]):
            return
        if directory:
            newobj = Directory(name=name, parent=self)
        else:
            newobj = File(name=name, file_size=size, parent=self)
        self.children.append(newobj)
        return newobj


@dataclass
class State():
    current_location: Directory
    filesystem_root: Directory
    directories: list[Directory] = field(default_factory=list)

    def process_cd(self, directory):
        match directory:
            case "..":
                self.current_location = self.current_location.parent
            case "/":
                self.current_location = self.filesystem_root
            case _:
                self.current_location = [
                    child for child in self.current_location.children if child.name == directory].pop(0)

    def process_ls(self, output: list[str]):
        for line in output:
            if line.startswith("dir"):
                newdir = self.current_location.create_child(
                    name=line.split(" ")[1], directory=True)
                self.directories.append(newdir)
            else:
                self.current_location.create_child(
                    name=line.split(" ")[1], size=int(line.split(" ")[0]))


if __name__ == "__main__":
    with open("../input.txt", "r") as infile:
        termlog = infile.readlines()
    root = Directory(name="root", parent=None)
    state = State(filesystem_root=root, current_location=root)
    while len(termlog) > 0:
        line = termlog.pop(0).strip()
        if line.startswith("$ cd"):
            state.process_cd(line.split(" ")[2])
        if line == "$ ls":
            lines = []
            while len(termlog) > 0 and not termlog[0].startswith("$"):
                lines.append(termlog.pop(0).strip())
            state.process_ls(lines)
    total_size = state.filesystem_root.size
    print(f"Total Size: {total_size}")
    dirsize = sum(
        [smdir.size for smdir in state.directories if smdir.size < 100000])
    print(f"Part1: {dirsize}")
    state.directories.sort(key=lambda directory: directory.size)
    free = 70000000 - total_size
    needed = 30000000 - free
    for ob in state.directories:
        if ob.size >= needed:
            print(ob.size)
            break
    pass
