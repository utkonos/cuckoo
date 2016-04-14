# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import argparse
import logging
import os
import sys
import traceback

from cuckoo.common.exceptions import CuckooCriticalError
from cuckoo.common.logo import logo
from cuckoo.common.utils import exception_message
from cuckoo.core.database import Database
from cuckoo.core.resultserver import ResultServer
from cuckoo.core.scheduler import Scheduler
from cuckoo.core.startup import check_configs
from cuckoo.core.startup import check_version, create_structure
from cuckoo.core.startup import cuckoo_clean, drop_privileges
from cuckoo.core.startup import init_logging, init_modules
from cuckoo.core.startup import init_tasks, init_yara, init_binaries
from cuckoo.core.startup import init_rooter, init_routing
from cuckoo.misc import set_cwd

log = logging.getLogger("cuckoo")

def cuckoo_init(quiet=False, debug=False):
    """Initialize Cuckoo configuration.
    @param quiet: enable quiet mode.
    @param debug: enable debug mode.
    """
    logo()
    check_configs()
    check_version()
    create_structure()

    init_logging()

    if quiet:
        log.setLevel(logging.WARN)
    elif debug:
        log.setLevel(logging.DEBUG)

    init_modules()
    init_tasks()
    init_yara()
    init_binaries()
    init_rooter()
    init_routing()

    Database().connect()
    ResultServer()

def cuckoo_main(max_analysis_count=0):
    """Cuckoo main loop.
    @param max_analysis_count: kill cuckoo after this number of analyses
    """
    try:
        sched = Scheduler(max_analysis_count)
        sched.start()
    except KeyboardInterrupt:
        sched.stop()

def cuckoo():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", help="Run a subcommand")
    parser.add_argument("-q", "--quiet", help="Display only error messages", action="store_true", required=False)
    parser.add_argument("-d", "--debug", help="Display debug messages", action="store_true", required=False)
    parser.add_argument("--user", type=str, help="Drop user privileges to this user")
    parser.add_argument("--root", type=str, default="~/.cuckoo", help="Cuckoo Working Directory")
    args = parser.parse_args()

    set_cwd(os.path.expanduser(args.root))

    if args.user:
        drop_privileges(args.user)

    if args.command == "clean":
        cuckoo_clean()
        sys.exit(0)

    try:
        cuckoo_init(quiet=args.quiet, debug=args.debug)
        cuckoo_main(max_analysis_count=args.max_analysis_count)
    except CuckooCriticalError as e:
        message = "{0}: {1}".format(e.__class__.__name__, e)
        if len(log.handlers):
            log.critical(message)
        else:
            sys.stderr.write("{0}\n".format(message))
        sys.exit(1)
    except:
        # Deal with an unhandled exception.
        message = exception_message()
        print message, traceback.format_exc()
