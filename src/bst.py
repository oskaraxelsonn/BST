#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)


class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children..
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''

        if self.is_empty():
            return False

        if self.get_value == v():
            return True

        if self.get_value > v():
            return self.get_lc().is_member(v)
        else:
            return self.get_rc().is_member(v)
        # return False
        # ska kolla om jag behöver en return false ifall den inte hittar

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        logging.info("TODO@src/bst.py: implement size()")
        return 0

    def height(self):
        '''
        Returns the height of the tree.
        '''
        logging.info("TODO@src/bst.py: implement height()")
        return 0

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        log.info("TODO@src/bst.py: implement inorder()")
        return []

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        log.info("TODO@src/bst.py: implement postorder()")
        return []

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''

        if self.is_empty():
            return []

        log.info("TODO@src/bst.py: implement bfs_order_star()")
        return []

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        log.info("TODO@src/bst.py: implement delete()")
        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
