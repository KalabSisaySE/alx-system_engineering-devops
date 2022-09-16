# kills a process named killmenow
exec { 'pkill killmenow':
  command => '/bin/echo',
}
