
#!/bin/sh
file="$1"
dependencies="pdftohtml gnuhtml2latex pdflatex"
echo "PDF to LaTeX conversion script"
echo "Copyleft 2012 (c) Tom Van Braeckel <tomvanbraeckel@gmail.com>"
echo
echo "WARNING: this is a rudimentary first stab. Proceed with caution."
echo
if [ -z "$file" ]; then
 echo "Usage: $0 <pdf file>"
 echo "The resulting .tex file will be stored somewhere here."
 exit 1
fi
echo

echo "Checking if all dependencies are found..."
for dependency in $dependencies; do
 which $dependency
 if [ $? -ne 0 ]; then
  echo "Dependency $dependency not found, install it using:"
  echo "sudo apt-get install $dependency"
  exit 1
 else
  echo "Dependency $dependency found."
 fi
done
echo

echo "Converting $file to ${file}s.html"
pdftohtml -nomerge "$file" "$file".html
echo

echo "Fixing up ${file}s.html to ${file}_fixedup.html..."
# This nasty br in a b causes problems later on
sed "s,<br/></b>,</b><br/>,g" "${file}s.html" > "${file}_fixedup.html"
# ending with bold text menas it is the end of a title and can be on a newline
sed -i "s,</b><br/>\$,</b><br/><br/>,g" "${file}_fixedup.html"
# starting with bold text means it is the start of a title so can be on a new line
sed -i "s,^<b>,<br/><b>,g" "${file}_fixedup.html"
# spaces ?
sed -i "s,\&#160;, ,g" "${file}_fixedup.html"
# there is no use in a space before a newline, and it causes a bogus indent when converting to .tex later on
sed -i "s, <br/>,<br/>,g" "${file}_fixedup.html"
# encoding, although gnuhtml2latex ignores this
sed -i "s,<HEAD>,<HEAD><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />," "${file}_fixedup.html"
echo

echo "Readying ${file}_fixedup.html for tex conversion in ${file}_fixedup_ready_for_tex_conversion.html"
cp "${file}_fixedup.html" "${file}_fixedup_ready_for_tex_conversion.html"
# br is ignored and should be replaced by a newline
sed -i "s,<br/>,<p></p>,g" "${file}_fixedup_ready_for_tex_conversion.html"
# Remove bogus links - this fixes the empty } problem
sed -i "s/<A name=[0-9]\+><\/a>//g" "${file}_fixedup_ready_for_tex_conversion.html"
echo

echo "Converting ${file}_fixedup_ready_for_tex_conversion.html to ${file}_frompdf.tex"
# -c = table of contents
# -s = write to standard out
# -p  Break page after title / table of contents
# -H  use hyperref package to process anchors
# -g images
# -n  Use numbered sections
gnuhtml2latex -c -s -p -H -n "${file}_fixedup_ready_for_tex_conversion.html" > "$file"_frompdf.tex
echo "The resulting file is in ${file}_frompdf.tex"
echo

echo "Fixing up ${file}_frompdf.tex to ${file}_frompdf_fixedup.tex"
sed -i 's/\\par/\\newline/g' "${file}_frompdf.tex"
( cat header.inc ; tail -n +7 "${file}_frompdf.tex" ) > "${file}_frompdf_fixedup.tex"
echo

echo "Converting ${file}_frompdf_fixedup.tex to ${file}_frompdf_fixedup.pdf for inspection..."
pdflatex -interaction nonstopmode "${file}_frompdf_fixedup.tex" > tex_to_pdf_errors_and_warnings.txt
echo

echo "Opening ${file}_frompdf_fixedup.pdf with Evince - you can try another PDF viewer if you like..."
evince "$file"_frompdf_fixedup.pdf

