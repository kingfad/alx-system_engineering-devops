# Install and configure Nginx
package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

file {'Configure the home page':
  ensure    => 'present',
  path      => '/var/www/html/index.nginx-debian.html',
  content   => 'Hello World\n'
}

file_line {'Redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
