
from __future__ import print_function

import os
import sys


########
# Main #
########
if __name__ == '__main__':
    print("""script/SimpleGUICS2Pygame_check.py (January 13, 2016)
=====================================================""")

    # Environment variables
    print('PATH:')
    path_str = os.getenv('PATH')
    if path_str is not None:
        for path in path_str.split(os.pathsep):
            print(' ', path)

    print()

    print('PYTHONPATH:')
    path_str = os.getenv('PYTHONPATH')
    if path_str is not None:
        for path in path_str.split(os.pathsep):
            print(' ', path)

    print('\n')

    # Python
    print('python - version', sys.version, end='\n\n')

    print('sys.path:')
    for path in sys.path:
        print(' ', path)

    print('\n')

    # matplotlib
    CMD = 'import matplotlib'
    try:
        import matplotlib

        print(CMD, 'ok - Version', matplotlib.__version__)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print('\n')

    # Pygame
    CMD = 'import pygame'
    try:
        import pygame

        print(CMD, 'ok - Version', pygame.version.ver)

        CMD = 'pygame.init()'
        try:
            SUCCESS, FAILED = pygame.init()

            if FAILED == 0:
                print(' ', CMD, SUCCESS, 'modules loaded ok')
            else:
                print(' ', CMD, SUCCESS, 'modules loaded',
                      FAILED, 'failed WARNING!')
        except Exception as exc:
            print(' ', CMD, 'FAILED!', exc)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print('\n')

    # simplegui
    CMD = 'import simplegui'
    try:
        import simplegui

        print(CMD, """PROBLEM - The package simplegui is installed!
  It is a Python package which has the same name as SimpleGUI of CodeSkulptor,
  but it is totally something else.
  If you don't uninstall it,
  you must replace the recommended import of SimpleGUICS2Pygame.

""")
    except Exception as exc:
        pass

    # SimpleGUITk
    CMD = 'import simpleguitk'
    try:
        import simpleguitk

        print(CMD, """WARNING - The package simpleguitk is installed!
  It is another implementation of SimpleGUI of CodeSkulptor,
  using Tkinter and some others packages.
  If you don't uninstall it,
  you must be careful with the import of SimpleGUICS2Pygame.

""")
    except Exception as exc:
        pass

    # SimpleGUICS2Pygame
    CMD = 'import SimpleGUICS2Pygame'
    try:
        import SimpleGUICS2Pygame

        print(CMD, 'ok - Version', SimpleGUICS2Pygame._VERSION)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print()

    CMD = 'import SimpleGUICS2Pygame.codeskulptor'
    try:
        import SimpleGUICS2Pygame.codeskulptor

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.codeskulptor_lib'
    try:
        import SimpleGUICS2Pygame.codeskulptor_lib

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.numeric'
    try:
        import SimpleGUICS2Pygame.numeric

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib'
    try:
        import SimpleGUICS2Pygame.simplegui_lib

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_draw'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_draw

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_fps'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_fps

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_keys'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_keys

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_loader'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_loader

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simpleguics2pygame'
    try:
        import SimpleGUICS2Pygame.simpleguics2pygame

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simpleplot'
    try:
        import SimpleGUICS2Pygame.simpleplot

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)
