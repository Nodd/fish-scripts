#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
try:
    from path import path

    try:
        from shutil import which
    except NameError:
        import os

        # https://hg.python.org/cpython/file/6860263c05b3/Lib/shutil.py#l1068
        def which(cmd, mode=os.F_OK | os.X_OK, path=None):
            """Given a command, mode, and a PATH string, return the path which
            conforms to the given mode on the PATH, or None if there is no such
            file.

            `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
            of os.environ.get("PATH"), or can be overridden with a custom search
            path.

            """
            # Check that a given file can be accessed with the correct mode.
            # Additionally check that `file` is not a directory, as on Windows
            # directories pass the os.access check.
            def _access_check(fn, mode):
                return (os.path.exists(fn) and os.access(fn, mode) and
                        not os.path.isdir(fn))

            # If we're given a path with a directory part, look it up directly
            # rather than referring to PATH directories. This includes checking
            # relative to the current directory, e.g. ./script
            if os.path.dirname(cmd):
                if _access_check(cmd, mode):
                    return cmd
                return None

            if path is None:
                path = os.environ.get("PATH", os.defpath)
            if not path:
                return None
            path = path.split(os.pathsep)

            # On other platforms you don't have things like PATHEXT to tell you
            # what file suffixes are executable, so just pass on cmd as-is.
            files = [cmd]

            seen = set()
            for dir in path:
                normdir = os.path.normcase(dir)
                if normdir not in seen:
                    seen.add(normdir)
                    for thefile in files:
                        name = os.path.join(dir, thefile)
                        if _access_check(name, mode):
                            return name
            return None

    hosts_content = path("/etc/hosts").lines(encoding="utf8", errors="ignore")

    hosts = set()

    for line in hosts_content:
        # Suppression des commentaires
        line = line.split("#", 1)[0].strip()
        if not line:
            continue

        names = line.split()[1:]
        for name in names:
            if "." not in name and name != "localhost" and not which(name):
                hosts.add(name)

    for name in hosts:
        print(name)
except:
    pass
