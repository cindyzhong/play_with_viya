echo 'Closing the session ...'
curl -n -u sasdemo -X DELETE  http://localhost:8777/cas/sessions/$1
