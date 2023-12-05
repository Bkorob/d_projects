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
        self.state.get_current_state()

    def disconnect(self):
        self.state = self.tcp_states['disconnected'](self)

    def write(self, data):
        self.state.write(data)
        
    
class DisconnectedState:
    def __init__(self, name):
        self.name = name

    def connect(self):
        self.name.state = self.name.tcp_states['connected'](self)

    def get_current_state(self):
        raise TcpConnectionError("Already disconnected")

    def disconnect(self):
        raise TcpConnectionError("Already disconnected")

    def write(self, data):
        raise TcpConnectionError("Cannot write in closed state")
    
    
