import sys
import paramiko
from paramiko import SSHClient

ipClient = ''
usernameClient = ''
passwordClient = ''

class SSH(self):
    # Interface de comunicação SSH2
    sshSession = paramiko.SSHClient()
    # Leitura das Chaves cadastradas no ~/.ssh/known_hosts
    sshSession.ssh.load_system_host_keys()
    # O Que fazer quando uma chave não é encontrada?
    # Aceitar automaticamente as chaves e cadastrar no known_hosts
    sshSession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #Efetua conexão
    sshSession.connect(ipClient, username=usernameClient,
                    password=passwordClient)
    check_connection()
    
    def check_connection(self):
        """
        This will check if the connection is still availlable.

        Return (bool) : True if it's still alive, False otherwise.
        """
        try:
            self.ssh.exec_command('ls', timeout=5)
            return True
        except Exception as e:
            print "Connection lost : %s" %e
            return False

if __name__ = '__main__':
    sshSession = SSH(self)
