#!/usr/bin/env python
import os
import sys
import time

# A class that represents the individual node of the Binary tree
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# A function to display the leaf nodes.
def counter(root):
    if root:
        if root.left == None and root.right == None:
            print(root.data)
        # First recur the left child
        if root.left:
            counter(root.left)
        # Recur the right child at last
        if root.right:
            counter(root.right)


# run the counter function while passing the root as the argument to print all the leaf nodes of a binary tree!
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mac.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
