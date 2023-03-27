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
    """Validate that ansible user is not sudoer"""
    etc_sudoers_d_ansible = host.file("/etc/sudoers.d/ansible")
    assert not etc_sudoers_d_ansible.exists


def test_ansible_no_ssh(host):
    """Validate that ansible user has no authorized_keys"""
    opt_ansible_authorized_keys = host.file("/opt/ansible/.ssh/authorized_keys")
    assert not opt_ansible_authorized_keys.exists
