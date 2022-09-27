# This script automate the task of creating a custom HTTP header response

package { 'nginx':
  ensure  => 'installed',
}

file_line {'new':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => '# server_name_in_redirect off;',
  line   => 'add_header X-Served-By $HOSTNAME;',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}

