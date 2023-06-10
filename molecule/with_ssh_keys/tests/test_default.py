"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_ansible_user_group(host):
    """Validate ansible user and group."""
    ansible_group = host.group("ansible")
    ansible_user = host.user("ansible")
    assert ansible_group.exists
    assert ansible_user.exists
    assert ansible_user.group == "ansible"
    assert ansible_user.shell == "/bin/bash"

def test_ansible_sudoer(host):
    """Validate that ansible user is sudoer"""
    etc_sudoers_d_ansible = host.file("/etc/sudoers.d/ansible")
    assert etc_sudoers_d_ansible.exists
    assert etc_sudoers_d_ansible.user == "root"
    assert etc_sudoers_d_ansible.group == "root"
    assert etc_sudoers_d_ansible.mode == 0o440
    assert etc_sudoers_d_ansible.contains("ansible ALL=NOPASSWD:SETENV: ALL")

def test_ansible_ssh_authorized_keys(host):
    """Validate that ansible user has authorized_keys"""
    opt_ansible_authorized_keys = host.file("/opt/ansible/.ssh/authorized_keys")
    assert opt_ansible_authorized_keys.exists
    assert opt_ansible_authorized_keys.user == "ansible"
    assert opt_ansible_authorized_keys.group == "ansible"
    assert opt_ansible_authorized_keys.mode == 0o600
    assert opt_ansible_authorized_keys.contains("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIClfmTk73wNNL2jwvhRUmUuy80JRrz3P7cEgXUqlc5O9 ansible@instance")
