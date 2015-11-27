$path = "C:\Users\Kevin\Desktop\psych-study\photos_output\"
cd $path

$files = gci "*.tex"

# check all TeX files in the $files array
foreach ($i in $files) {
   # Name of the PDF file
   $pdfpath = $path + $i.BaseName + ".pdf"

   if (Test-Path -path $pdfpath){
           "A PDF for $i exists"
           $pdf = gci $pdfpath
           if ($i.LastWriteTime -gt $pdf.LastWriteTime) {
              "TeX file is newer, let's create the PDF!"
              pdflatex $i
          }
          else {
              "but the PDF is newer, so no compilation is needed"
          }

      } else {
            "No PDF found for $i, let's create it!"
             pdflatex $i
      }
}

get-childitem $path -include *.aux -recurse | foreach ($_) {remove-item $_.fullname}
get-childitem $path -include *.log -recurse | foreach ($_) {remove-item $_.fullname}
get-childitem $path -include *.tex -recurse | foreach ($_) {remove-item $_.fullname} 

#Dir | Rename-Item –NewName { $_.name –replace “photo“,”set” }