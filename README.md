Takes a Webrequest and returns a PDF file

$response = Invoke-WebRequest -Method POST -Uri "https://doc2pdf-3yvuhaorjq-uc.a.run.app/convert_doc_to_pdf" -InFile "MakeMeAPDF.docx"

Invoke-WebRequest -Method POST -Uri https://doc2pdf-3yvuhaorjq-uc.a.run.app/convert_doc_to_pdf -InFile "MakeMeAPDF.docx"

Invoke-WebRequest -Uri https://doc2pdf-3yvuhaorjq-uc.a.run.app

$FilePath = "C:\Users\devin\Desktop\Notes.docx";
$URL = "https://localhost:8080/convert_doc_to_pdf";

$fileBytes = [System.IO.File]::ReadAllBytes($FilePath);
$fileEnc = [System.Text.Encoding]::GetEncoding('UTF-8').GetString($fileBytes);
$boundary = [System.Guid]::NewGuid().ToString(); 
$LF = "`r`n";

$bodyLines = ( 
    "--$boundary",
    "Content-Disposition: form-data; name=`"file`"; filename=`"NOTES.docx`"",
    "Content-Type: application/octet-stream$LF",
    $fileEnc,
    "--$boundary--$LF" 
) -join $LF

Invoke-RestMethod -Uri $URL -Method Post -ContentType "multipart/form-data; boundary=`"$boundary`"" -Body $bodyLines



THIS (BELOW) WORKS WITH TXT FILE

$FilePath = "TestFile.txt";
$URL = "http://localhost:8080/convert_doc_to_pdf";


$fileBytes = [System.IO.File]::ReadAllBytes($FilePath);
$fileEnc = [System.Text.Encoding]::GetEncoding('UTF-8').GetString($fileBytes);
$boundary = [System.Guid]::NewGuid().ToString(); 
$LF = "`r`n";

$bodyLines = ( 
    "--$boundary",
    "Content-Disposition: form-data; name=`"file`"; filename=`"TestFile.txt`"",
    "Content-Type: application/octet-stream$LF",
    $fileEnc,
    "--$boundary--$LF" 
) -join $LF

Invoke-RestMethod -Uri $URL -Method Post -ContentType "multipart/form-data; boundary=`"$boundary`"" -Body $bodyLines