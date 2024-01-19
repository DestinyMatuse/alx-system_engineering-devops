# install_python_flask_werkzeug.pp

# Install python3-pip package
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

# Install Werkzeug 2.1.1 using pip3
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path    => ['/usr/bin'],
  require => Exec['install_flask'],
}

