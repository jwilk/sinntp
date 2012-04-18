XSL = http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
XSLTPROC = xsltproc --nonet --param man.charmap.use.subset 0

XML_FILES = $(wildcard *.xml)
MAN_FILES = $(XML_FILES:.xml=.1)

.PHONY: all
all: $(MAN_FILES)

%.1: %.xml
	$(XSLTPROC) $(XSL) $(<)
	sed -i -e  '/^[.]TH/ { s/"[0-9/]\{10\}"/"$(shell date +%F)"/ }' $(@)

.PHONY: clean
clean:
	rm -f $(MAN_FILES)

# vim:ts=4
