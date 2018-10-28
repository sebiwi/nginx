import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(host):
    nginx = host.package('nginx')
    assert nginx.is_installed


def test_nginx_is_running(host):
    nginx = host.service('nginx')
    assert nginx.is_running


def test_nginx_says_hello(host):
    host.run_expect([0], 'curl localhost/hello | grep conf')
