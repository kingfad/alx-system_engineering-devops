# Kill the killmenow process
exec { 'stop killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
