#!/usr/bin/python3
# coding: utf-8
# License: The MIT License
# Author: Alexander Lutsai <s.lyra@ya.ru>
# Year: 2021
# Description: This launches script that draws menu to choose, mount and unmount drives from ranger file manager

from ranger.api.commands import Command


class mount(Command):
    """:mount

    Show menu to mount and unmount
    """

    def execute(self):
        """ Show menu to mount and unmount """
        self.fm.execute_console(
            "shell python3 ~/.config/ranger/ranger_udisk_menu/menu.py")
