# Creates a file with content
file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
