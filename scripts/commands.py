from cuwo.script import (FactoryScript, ProtocolScript, command, get_player,
    admin)
from cuwo.common import get_chunk
import platform

class CommandFactory(FactoryScript):
    def on_load(self):
        pass

    def on_unload(self):
        pass

def get_class():
    return CommandFactory

@command
@admin
def say(script, *args):
    message = ' '.join(args)
    script.protocol.send_chat(message)

@command
def server(script):
    return 'Server is running on %r' % platform.system()

@command
def login(script, password):
    password = password.lower()
    user_types = script.factory.passwords.get(password, [])
    if not user_types:
        return 'Invalid password'
    script.protocol.rights.update(user_types)
    return 'Logged in as %s' % (', '.join(user_types))

@command
@admin
def kick(script, name):
    player = get_player(script.factory, name)
    player.kick()

@command
def whereis(script, name = None):
    if name is None:
        player = script.protocol
        message = 'You are at %s'
    else:
        player = get_player(script.factory, name)
        message = '%s is at %%s' % player.get_name()
    return message % (get_chunk(player.get_position()),)
