This python script can be used to automate "signal newnym" process of TOR to request new IP address eq. change it's exit node. <br/>
Things you should take care of:
<ul>
<li>Script needs <b>python-socksipy</b> package to be installed
<li>Be sure to edit the password in the script 
<li>Remember also set the controlport and password in torrc config file, in Debian this can be found from <b>/etc/tor/torrc</b>
<li>You can generate the hash needed for HashedControlPassword directive in torrc with <b>tor --hash-password placeyourpwdhere</b>

