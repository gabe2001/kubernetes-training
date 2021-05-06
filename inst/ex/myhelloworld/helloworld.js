//Load express module with `require` directive

var express = require('express')
var app = express()
var os = require("os");

var server_port = process.env.OPENSHIFT_NODEJS_PORT || 8080
var server_ip_address = process.env.OPENSHIFT_NODEJS_IP || '127.0.0.1'

// Let's keep score of the visitor count

var visitorCount = 0;

// Define request response in root URL (/)

app.use(express.static('public')) ;

app.get('/health', function (req,res) {
   res.send('All is well') ;
   res.end() ;
})


app.get('/', function (req, res) {

  var visitorAddr ; 
  var hostname = os.hostname();

  visitorCount++ ;
   
  visitorAddr = req.connection.remoteAddress ;
  visitorAddr = visitorAddr.replace(/^.*:/, '') ;
  res.send('<img src="/Astro.png" width=400px><H1>Hello World!</H1><br>Serving you from '+hostname+' <br>You are visitor: #'+visitorCount+' and coming from '+visitorAddr+'<br>') ;
  res.end() ;
})

  //Launch listening server on port 8080
app.listen(server_port,function () {
  console.log('app listening on port 8080!')
})

