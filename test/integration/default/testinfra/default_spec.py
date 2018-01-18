def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_socket_listening(Socket):
    socket = Socket('tcp://127.0.0.1:80')
    assert socket.is_listening

def test_command_output(Command):
    command = Command('curl https://www.google.com')
    assert 'oved' in command.stdout
    assert command.rc == 0

# def test_nginx_running_and_enabled(host):
#     nginx = host.service("nginx")
#     assert nginx.is_running
#     assert nginx.is_enabled
# 
