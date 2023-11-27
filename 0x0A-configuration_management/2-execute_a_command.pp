# Kills a running process

exec { 'killmenow':
    command => 'pkill -f killmenow',
    path    =>  '/bin:usr/bin',
}