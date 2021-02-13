<h1 align="center">
  <br>
  <a href="https://github.com/sinsinsecurity/Priest"><img src="https://i.ibb.co/2Kmc5k3/2021-02-13-13-16-29.png" alt="Arjun">
  <img src="https://i.ibb.co/9YvFQcq/2021-02-13-12-30-20.png" alt="Arjun">
  </a>
</h1>





### What is this PoC?

------------


PHPinfo() displays the content of any variables such as `$_GET, $_POST and $_FILES`.

> By making multiple upload posts to the PHPInfo script, and carefully controlling the reads, it is possible to retrieve the name of the temporary file and make a request to the LFI script specifying the temporary file name.

this PoC is a working exploit for the vulnerability found by Brett Moore from https://insomniasec.com/ which exploit the Local File Inclusion vulnerability with arbitrary files uploaded through a phpinfo.php page, you just need to find 2 components, the first one is a vulnerable Local File Inclusion page on the target and the other is a page like example.php containing the code `<?php phpinfo(); ?>`

Research from https://insomniasec.com/


### How to use?

------------


if you don't know the concept at all feel free to read these articles

https://insomniasec.com/cdn-assets/LFI_With_PHPInfo_Assistance.pdf

it will run the command `<?php system('calc.exe') ?>` on the target web server feel free to edit the file and change the command that gets executed
you'll be needing 2 things:
- http://192.168.1.1/phpinfo.php
- http://192.168.1.1/LFI.php?vulnerable_parameter=

<h6 align="center">
  <br>
  <a href="https://i.ibb.co/f8c0n7F/carbon.png"><img src="https://i.ibb.co/f8c0n7F/carbon.png" alt="Arjun"></a>
</h6>


#### Usage

------------


```
git clone https://github.com/sinsinsecurity/phpinfo-Local-File-Inclusion.git
cd phpinfo-Local-File-Inclusion
python phpinfo-LFI-PoC.py 17
```



