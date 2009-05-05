# silly hack, i can't be bothered debugging my broken django templates

homepage = """
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<style type="text/css" src="/static/default.css">
</style>
</head>
<body style="background-color:#000000;color:#A00000;">
<table style="border:none;margin-left:auto; margin-right:auto;">
<tr><td valign="center">
<img style="margin-left:auto;margin-right:auto;" src="/static/nin_logo.png" alt="NIN"/>
</td></tr>

<tr>
<th>Photo blog</th>
<th>News</th>
</tr>

<tr>
<td>
<div style="text-align:center;">
<img src="%s" width="120" height="120" alt="photo blog"/> 
%s
</div>

</td>
<td>&nbsp;</td>
</tr>

</table>
</body>
</html>

"""
