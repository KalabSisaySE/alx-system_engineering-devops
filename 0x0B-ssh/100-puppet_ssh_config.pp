# configures the client SSH configuration 
# to disable password authentication 
# and setup a private key

class { 'ssh::client':
  options => {
    'Host 18.208.143.155' => {
      'PasswordAuthentication' => 'no'
      'IdentityFile'           => '~/.ssh/id_rsa'
    }
  }
}
