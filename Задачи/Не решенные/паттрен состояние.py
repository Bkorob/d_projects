import pytest


class TcpConnection:
    def __init__(self, *args):
        self.tcp_states = {
            'connected': ConnectedState,
            'disconnected': DisconnectedState,
        }
        self.state = self.tcp_states['disconnected'](self)

    def connect(self):
        self.state.connect()

    def get_current_state(self):
        return self.state.get_current_state()

    def disconnect(self):
        if self.state.get_current_state() == 'disconnected':
            raise TcpConnectionError('[eq')
        self.state = self.tcp_states['disconnected'](self)

    def write(self, data):
        self.state.write(data)


class DisconnectedState:
    def __init__(self, name):
        self.name = name
        self.status = 'disconnected'

    def connect(self):
        self.name.state = self.name.tcp_states['connected'](self)

    def get_current_state(self):
        return self.status

    def disconnect(self):
        raise TcpConnectionError("Already disconnected")

    def write(self, data):
        raise TcpConnectionError("Cannot write in closed state")
    
    

class ConnectedState:
    def __init__(self, name):
        self.name = name

    def connect(self):
        raise TcpConnectionError("Already connected")

    def get_current_state(self):
        self.status = 'connected'
        return self.status

    def write(self, data):
        pass

    def disconnect(self):
        pass


class TcpConnectionError(Exception):
    pass


def test_connect1():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    print(connection.get_current_state())
    assert connection.get_current_state() == 'connected'
    connection.write('one')
    connection.write('two')
    connection.disconnect()
    assert connection.get_current_state() == 'disconnected'


def test_connect2():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    with pytest.raises(TcpConnectionError):
        connection.connect()


def test_connect3():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    connection.disconnect()
    print(connection.state)
    with pytest.raises(TcpConnectionError):
        connection.disconnect()


def test_connect4():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    connection.disconnect()
    with pytest.raises(TcpConnectionError):
        connection.write('one')
