XSL = http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
XSLTPROC = xsltproc --nonet --param man.charmap.use.subset 0

XML_FILES = $(wildcard *.xml)
MAN_FILES = $(XML_FILES:.xml=.1)

.PHONY: all
all: $(MAN_FILES)

%.1: %.xml
	$(XSLTPROC) $(XSL) $(<)
	perl -pi -e '/^[.]TH\b/ and s,"[0-9/]{10}","$(shell date +%F)",' $(@)

.PHONY: clean
clean:
	rm -f $(MAN_FILES)

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
