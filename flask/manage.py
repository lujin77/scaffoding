#!/usr/bin/env python
# encoding: utf-8
from flask_script import Manager, Server
from flask_script.commands import ShowUrls

from commands import GEventServer, ProfileServer
from application import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='mode', required=False, help="valid: dev test pro")
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))
manager.add_command("showurls", ShowUrls())
manager.add_command("gevent", GEventServer())
manager.add_command("profile", ProfileServer())


if __name__ == "__main__":
    manager.run()
