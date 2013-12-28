This python script can be used to automate "signal newnym" process of TOR to request new IP address eq. change it's exit node. <br/>
Things you should take care of:
<ul>
<li>be sure to edit the password in the script 
<li>remember also set the controlport and password in torrc config file, in Debian this can be found from /etc/tor/torrc
<li>you can generate the hash needed for HashedControlPassword directive in torrc with tor --hash-password placeyourpwdhere

