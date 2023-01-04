Takes a Webrequest and returns a PDF file

$response = Invoke-WebRequest -Method POST -Uri "https://doc2pdf-3yvuhaorjq-uc.a.run.app/convert_doc_to_pdf" -InFile "MakeMeAPDF.docx"

Invoke-WebRequest -Method POST -Uri https://doc2pdf-3yvuhaorjq-uc.a.run.app/convert_doc_to_pdf -InFile "MakeMeAPDF.docx"

Invoke-WebRequest -Uri https://doc2pdf-3yvuhaorjq-uc.a.run.app

$FilePath = "FL2F WS - Reduced Flow.docx";
$URL = "https://doc2pdf-3yvuhaorjq-uc.a.run.app/convert_doc_to_pdf";

$fileBytes = [System.IO.File]::ReadAllBytes($FilePath);
$fileEnc = [System.Text.Encoding]::GetEncoding('UTF-8').GetString($fileBytes);
$boundary = [System.Guid]::NewGuid().ToString(); 
$LF = "`r`n";

$bodyLines = ( 
    "--$boundary",
    "Content-Disposition: form-data; name=`"file`"; filename=`"FL2F WS - Reduced Flow.docx`"",
    "Content-Type: application/octet-stream$LF",
    $fileEnc,
    "--$boundary--$LF" 
) -join $LF

Invoke-RestMethod -Uri $URL -Method Post -ContentType "multipart/form-data; boundary=`"$boundary`"" -Body $bodyLines