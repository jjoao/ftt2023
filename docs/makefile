all: index.html sebenta.pdf

index.html: diario.md
	pandoc diario.md -s -o index.html

sebenta.pdf: sebenta.md
	pandoc -V geometry:a4paper,margin=2cm -V numbersections --toc -t pdf 'sebenta.md'  -o sebenta.pdf
