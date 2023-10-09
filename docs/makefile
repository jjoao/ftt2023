all: index.html sebenta.pdf

index.html: diario.md
	pandoc diario.md -s -o index.html

sebenta.pdf: sebenta.md
	pandoc -V geometry:a4paper,margin=2cm -V numbersections --toc -t pdf 'sebenta.md'  -o sebenta.pdf
	
d:
	- rm index.html sebenta.pdf
	make all

pull:
	- rm index.html sebenta.pdf
	git pull
	make all

install:
	make pull
#	git add .
	git commit -a -m "installing"
	git push
