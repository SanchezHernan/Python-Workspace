<html>
<head>
<title>Descarga Ya! </title>
<meta name='title' content='Musica '>
<meta name='Language' content='Spanish'>
<meta charset="utf-8" />
<meta name='robots' content='noindex,nofollow' /> 
<meta name='googlebot' content='noindex,nofollow' />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<meta name="referrer" content="no-referrer">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="expires" content="Sun, 01 Jan 2014 00:00:00 GMT"/>
<meta http-equiv="pragma" content="no-cache" />
<link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon">
<base href="https://lagubr.com/">
<style>
#content{text-align: center;margin: 0 auto;}
#progress{display:none;color: #F00;font-size: 17px;font-weight: bold;font-style: oblique;font-family: Arial,Helvetica Neue,Helvetica,sans-serif;height: 50px;}
#download {display:none;color: #F00;font-size: 50px;font-style: normal;font-family: Arial,Helvetica Neue,Helvetica,sans-serif;height: 50px;}
#download a:link {font:Arial; font-size:50px; color:#FF0000;text-decoration: underline;}
#submit{text-decoration: none; background: black;border: none;color: #FFF;font-size: 50px; text-decoration: underline; font-style: normal;font-family: Arial,Helvetica Neue,Helvetica,sans-serif;height: 50px;cursor:pointer;}
#submit:hover{border:none; text-decoration: none;}
#title{margin: 10px 0 0 0;text-decoration: none;font-size: 20px;color: #A2A2A2;text-align: center;font-style: normal;font-family: Arial,Helvetica Neue,Helvetica,sans-serif;}
#load{display: block; margin: 0 auto; width: 120px; height: 15px;background:url(https://i.imgur.com/WTimZsJ.gif);} 
#notes{display:none;text-decoration: none;
font-size: 12px;
color: #FF5A00;
text-align: center;
font-style: normal;
font-family: Arial,Helvetica Neue,Helvetica,sans-serif;}
</style>

<script src="//code.jquery.com/jquery-latest.js" type="text/javascript"></script>




<script>
var qry = window.location.search;
var idquery = 'g5qU7p7yOY8';
var success = false;

var tmp = Math.random();


$.ajax({
    url: '//query.yahooapis.com/v1/public/yql',
    data: {
                    q: "select * from json where url ='http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="+idquery+"&format=json'",
                    format: "json"
                },
    dataType: 'json',
success: function(response){
        t = response.query.results.json.title;
	$('#title').html(t);
},
error: function(response) {
        window.setTimeout(function(){ document.location.reload(true); }, 10000);
    }
});




</script>
</head>
<body bgcolor="#000000">
    <p align="center">&nbsp;</p>
    <p align="center">&nbsp;</p>
 <div id="content">  
 <font face="Arial" size="5" color="#333333">Espere <b>0</b> segundos...</font>
  <div id="converter_wrapper">
   <div id="converter">
     <a id="submit" href="javascript:void()" rel="nofollow">DESCARGAR</a>
    <div id="progress">
     <span>Generando enlace de descarga...</span><br><i id="load"></i>
    </div>   
    <div id="download">
     <a id="file" href="" target="fluor" rel="nofollow">DESCARGAR</a>
    </div> 
    <div id="title">...
    </div>
   </div> 
   <br><span id="notes">Haga clic derecho y presione <b>"Guardar enlace como..."</b></span>
  </div>


 </div>
 <br><br><br><p><font color="#C0C0C0" size="2" style="font-family: Arial,Helvetica Neue,Helvetica,sans-serif;"><b>Nota:</b> Utilizamos el servicio que proporciona el sitio <b>https://ytmp3.cc/</b></font></p><iframe name="fluor" marginwidth="1" marginheight="1" width="0" height="0" scrolling="no" border="0" frameborder="0" src="about:banck"></iframe>
<iframe name="fluor" marginwidth="1" marginheight="1" width="0" height="0" scrolling="no" border="0" frameborder="0" src="about:blank"></iframe> 
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="//lagubr.com/api/door.js?2.3"></script>
<script>section=1000339897;popTimes=3;channel=4;captureFirstClick=true;</script><script src="//cdn.viralcpm.com/js/pop.js"></script></body>
</html>
