all: index.html notas.pdf

index.html: diario.md
		pandoc diario.md -s -o index.html

notas.pdf: notas.md
	pandoc -V geometry:a4paper,margin=2cm -V numbersections --toc -t pdf 'notas.md'  -o notas.pdf
