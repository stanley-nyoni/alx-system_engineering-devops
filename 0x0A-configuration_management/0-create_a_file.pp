# creates a file in the /tmp folder

file { '/tmp/school':
    ensure  => 'file',
    mode    => '0774',
    owner   => 'www.data',
    group   => 'www.data',
    content => 'I love Puppet',
}