#!/usr/bin/env python3
from dataclasses import dataclass
from typing import TypeVar, Mapping

# Generic type T
T = TypeVar("T")


@dataclass
class TrieNode[T]:
    """
    Node class for the Trie data structure.

    Attributes:
        value (str): The value of the node.
        children (dict): The children of the node.
    """

    value: T
    children: Mapping[str, "TrieNode"] = {}
    terminal: bool

    def insert(self, value: T) -> None:
        """
        Inserts a value into the Trie.

        Args:
            value (T): The value to be inserted.
        """
        node = self
        for i in range(len(value)):
            # If the next character is not in the children, add it.
            if node.children.get(value[i]) is None:
                node.children[value[i]] = TrieNode(value[i], {}, False)
            # Move to the next node.
            node = node.children.get(value[i])
        # Set the value and mark it as a terminal node.
        node.value = value
        node.terminal = True

    def trie_find(self, value: T) -> bool:
        node = self
        for i in range(len(value)):
            if node.children.get(value[i]) is None:
                return False
            node = node.children.get(value[i])
        return True


def trie_delete(node: TrieNode[T], value: T) -> None:
    if value is None:
        if node.terminal:
            node.terminal = False
            node.value = None
        for i in node.children.values():
            trie_delete(i, None)
        return

    for i in range(len(value)):
        if node.children.get(value[i]) is None:
            return
        node = node.children.get(value[i])
    if node.terminal:
        node.terminal = False
        node.value = None
    trie_delete(node, None)


def trie_dfs(node: TrieNode[T]) -> list[T]:
    if node.terminal:
        return [node.value]
    return [node.value] + sum([trie_dfs(i) for i in node.children.values()], [])


def longest_common_branch_trie(node1: TrieNode[T], node2: TrieNode[T]) -> list[T]:
    return [i for i in trie_dfs(node1) if i in trie_dfs(node2)]
